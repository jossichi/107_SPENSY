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

    <!-- Charts -->
    <div class="row mt-5">
      <div class="col-md-6">
        <h3 class="text-center">Comment Statistics</h3>
        <apexchart type="pie" :options="commentChartOptions" :series="commentChartSeries"></apexchart>
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
     
      commentChartSeries: [],
      postChartSeries: [],
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

      this.filteredData.forEach((item) => {
        const classification = String(item['Classification'] || '').trim();

        // Check for comment content and classify
        if (item['Comment Content']) {
          if (classification === 'Tích cực') {
            this.commentStats.positive++;
          } else if (classification === 'Tiêu cực') {
            this.commentStats.negative++;
          }
        }
        // Check for post content and classify
        else if (item['Post Content']) {
          if (classification === 'Tích cực') {
            this.postStats.positive++;
          } else if (classification === 'Tiêu cực') {
            this.postStats.negative++;
          }
        }
      });

      // Prepare data for pie charts
      this.commentChartSeries = [this.commentStats.positive, this.commentStats.negative];
      this.postChartSeries = [this.postStats.positive, this.postStats.negative];
    },

    updatePagination() {
      this.totalPages = Math.ceil(this.filteredData.length / this.itemsPerPage);
      this.paginateData();
    },

    paginateData() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      this.paginatedData = this.filteredData.slice(startIndex, endIndex);
    },

    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
        this.paginateData();
      }
    },

    filterData() {
      if (this.classificationFilter) {
        this.filteredData = this.tableData.filter(
          (item) => item['Classification'] === this.classificationFilter
        );
      } else {
        this.filteredData = this.tableData;
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
