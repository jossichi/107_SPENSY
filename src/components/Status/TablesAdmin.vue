<template>
    <div class="container mt-5">
      <h1 class="text-center">TablesAdmin</h1>
  
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
            <tr v-for="(item, index) in tableData" :key="index">
              <td>{{ item['User ID'] }}</td>
              <td>{{ item['Post ID'] }}</td>
              <td>{{ item['Post Content'] || 'N/A' }}</td>
              <td>{{ item['Comment Content'] || 'N/A' }}</td>
              <td>{{ item['Classification, Probability'] || 'N/A' }}</td>
              
              <td>{{ item['Translation Time'] || 'N/A' }}</td>
              <td>{{ item['Classification Time'] || 'N/A' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <!-- Charts -->
      <div class="row mt-5">
        <div class="col-md-6">
          <h3 class="text-center">Comment Statistics</h3>
          <apexchart type="pie" :options="commentChartOptions" :series="commentChartSeries"></apexchart>
        </div>
        <div class="col-md-6">
          <h3 class="text-center">Post Statistics</h3>
          <apexchart type="pie" :options="postChartOptions" :series="postChartSeries"></apexchart>
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
        commentStats: { positive: 0, negative: 0 },
        postStats: { positive: 0, negative: 0 },
        commentChartOptions: {
          chart: { type: 'pie' },
          labels: ['Positive Comments', 'Negative Comments'],
        },
        postChartOptions: {
          chart: { type: 'pie' },
          labels: ['Positive Posts', 'Negative Posts'],
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
            this.processData();
          })
          .catch((error) => {
            console.error("Error loading Excel file:", error);
          });
      },
  
      processData() {
        this.commentStats = { positive: 0, negative: 0 };
        this.postStats = { positive: 0, negative: 0 };
  
        this.tableData.forEach((item) => {
          if (item["Comment Content"]) {
            if (item["Classification"] === "Positive") {
              this.commentStats.positive++;
            } else if (item["Classification"] === "Negative") {
              this.commentStats.negative++;
            }
          } else if (item["Post Content"]) {
            if (item["Classification"] === "Positive") {
              this.postStats.positive++;
            } else if (item["Classification"] === "Negative") {
              this.postStats.negative++;
            }
          }
        });
  
        this.commentChartSeries = [this.commentStats.positive, this.commentStats.negative];
        this.postChartSeries = [this.postStats.positive, this.postStats.negative];
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
  </style>
  