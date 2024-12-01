<template>
  <div class="container mt-5">
    <h1 class="text-center">TablesAdmin</h1>

    <!-- Filter for classification -->
    <div class="d-flex justify-content-end mb-3">
      <label for="classification-filter" class="mr-2">Filter by Classification:</label>
      <select id="classification-filter" v-model="classificationFilter" @change="filterData">
        <option value="">All</option>
        <option value="Tích cực">Tích cực</option>
        <option value="Tiêu cực">Tiêu cực</option>
      </select>
    </div>

    <!-- Table to display data -->
    <div class="table-responsive">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Post ID</th>
            <th>Post Content</th>
            <th>Comment Content</th>
            <th>Classification</th>
            <th>Probability</th>
            <th>Translation Time</th>
            <th>Classification Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in paginatedData" :key="index">
            <td>{{ item['User ID'] }}</td>
            <td>{{ item['Post ID'] || 'N/A' }}</td>
            <td>{{ item['Post Content'] || 'N/A' }}</td>
            <td>{{ item['Comment Content'] || 'N/A' }}</td>
            <td>{{ item['Classification'] || 'N/A' }}</td>
            <td>{{ item['Probability'] || 'N/A' }}</td>
            <td>{{ item['Translation Time'] || 'N/A' }}</td>
            <td>{{ item['Classification Time'] || 'N/A' }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="d-flex justify-content-between mt-3">
      <button class="btn btn-primary" :disabled="currentPage === 1" @click="changePage(currentPage - 1)">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button class="btn btn-primary" :disabled="currentPage === totalPages" @click="changePage(currentPage + 1)">Next</button>
    </div>

    <!-- Charts Section (Both Charts Side by Side) -->
    <div class="row mt-5">
      <div class="col-md-6" v-if="commentChartSeries.length > 0">
        <h3 class="text-center">Comment Statistics</h3>
        <apexchart type="pie" :options="commentChartOptions" :series="commentChartSeries"></apexchart>
      </div>
      <div class="col-md-6" v-if="wordCountChartSeries.length > 0">
        <h3 class="text-center">Comments by Word Count</h3>
        <apexchart type="line" :options="wordCountChartOptions" :series="wordCountChartSeries"></apexchart>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { read, utils } from 'xlsx';
import VueApexCharts from 'vue3-apexcharts';

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      tableData: [],
      filteredData: [],
      classificationFilter: '',
      currentPage: 1,
      itemsPerPage: 10,
      commentStats: { positive: 0, negative: 0 },
      postStats: { positive: 0, negative: 0 },
      commentChartOptions: {
        chart: { type: 'pie' },
        labels: ['Positive Comments', 'Negative Comments'],
      },
      wordCountChartOptions: {
        chart: { type: 'line' },
        xaxis: { title: { text: 'Số từ' }, categories: [] }, // Word counts on x-axis
        yaxis: { title: { text: 'Số lượng bình luận' } }, // Comment counts on y-axis
        title: { text: 'Số lượng bình luận theo số từ' },
        tooltip: {
          shared: true,
          intersect: false,
          y: {
            formatter: (val) => {
              return `${val} bình luận`; 
            },
          },
        },
      },
      wordCountChartSeries: [],  // Initialize as empty array
      commentChartSeries: [],    // Initialize as empty array
      percentageData: [],
      commentCount: 0,
    };
  },
  methods: {
    fetchData() {
      axios
        .get('http://localhost:5000/get_comments_and_posts', { responseType: 'arraybuffer' })
        .then((response) => {
          const data = new Uint8Array(response.data);
          const workbook = read(data, { type: 'array' });
          const sheetName = workbook.SheetNames[0];
          const sheet = workbook.Sheets[sheetName];
          const jsonData = utils.sheet_to_json(sheet);
          this.tableData = jsonData;
          this.filteredData = jsonData; // Initialize filtered data
          this.processData();
          this.updatePagination();
        })
        .catch((error) => {
          console.error('Error loading Excel file:', error);
        });
    },
    processData() {
  this.commentStats = { positive: 0, negative: 0 };
  this.postStats = { positive: 0, negative: 0 };

  let wordCountStats = {};

  this.commentCount = 0;
  let minWordCount = Infinity;
  let maxWordCount = -Infinity;

  this.filteredData.forEach((item) => {
    const classification = String(item['Classification'] || '').trim();

    if (item['Comment Content']) {
      const commentContent = item['Comment Content'];
      this.commentCount++; // Increment the comment count

      // Count words in the comment (use split to get each word)
      const wordCount = commentContent.split(/\s+/).filter(Boolean).length;

      // Track the min and max word count
      minWordCount = Math.min(minWordCount, wordCount);
      maxWordCount = Math.max(maxWordCount, wordCount);

      // Update word count stats for each word count
      if (!wordCountStats[wordCount]) {
        wordCountStats[wordCount] = 0;
      }
      wordCountStats[wordCount]++;

      // Update classification stats for positive and negative comments
      if (classification === 'Tích cực') {
        this.commentStats.positive++;
      } else if (classification === 'Tiêu cực') {
        this.commentStats.negative++;
      }
    }
  });

  // Sort the word counts in ascending order
  const categories = Object.keys(wordCountStats).sort((a, b) => a - b);

  const binCount = Math.ceil(maxWordCount / 10);
  const wordCountBins = {};

  for (let i = 0; i < binCount; i++) {
    const binStart = i * 10;
    const binEnd = (i + 1) * 10 - 1;
    wordCountBins[`${binStart}-${binEnd}`] = 0;
  }

  // Group the word counts into the bins
  categories.forEach((wordCount) => {
    const binStart = Math.floor(wordCount / 10) * 10;
    const binEnd = binStart + 9;
    const binKey = `${binStart}-${binEnd}`;
    wordCountBins[binKey] += wordCountStats[wordCount];
  });

  // Prepare the X-axis categories and Y-axis data
  const wordCountBinsSorted = Object.keys(wordCountBins).sort((a, b) => a - b); // Ensure categories are sorted from 0 to max
  const wordCountBinCounts = wordCountBinsSorted.map((bin) => wordCountBins[bin]);

  // Update the chart data and labels
  this.wordCountChartOptions.xaxis.categories = wordCountBinsSorted;
  this.wordCountChartSeries = [{ name: 'Bình luận', data: wordCountBinCounts }];
  this.commentChartSeries = [this.commentStats.positive, this.commentStats.negative];
},

    updatePagination() {
      this.totalPages = Math.ceil(this.filteredData.length / this.itemsPerPage);
      this.changePage(1);
    },
    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
        this.paginatedData = this.filteredData.slice(
          (this.currentPage - 1) * this.itemsPerPage,
          this.currentPage * this.itemsPerPage
        );
      }
    },
    filterData() {
      if (this.classificationFilter === '') {
        this.filteredData = this.tableData;
      } else {
        this.filteredData = this.tableData.filter(
          (item) => item['Classification'] === this.classificationFilter
        );
      }
      this.processData();
      this.updatePagination();
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>


<style scoped>
.container {
  margin-top: 20px;
}

.table {
  text-align: center;
}

.chart {
  margin-top: 20px;
}
</style>
