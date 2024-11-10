<template>
  <body data-spy="scroll" data-target="#scrollspy">
    <div class="main_figur">
      <section id="about" class="about colorsbg">
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-12">
              <div class="main_about_area">
                <div class="head_title text-center">
                  <h2>Giới thiệu</h2>
                </div>
                <div
                  class="about_content colorstext2 wow fadeInUp"
                  data-wow-duration="700ms"
                >
                  <div class="row">
                    <div class="col-sm-9 col-sm-offset-1">
                      <div class="single_abt single_about">
                        <h3>107 SPENSY</h3>
                        <p class="text-uppercase colorstext">LỜI CẢM ƠN</p>
                        <p class="special_thanks">
                          Hoàn thành khóa luận tốt nghiệp không chỉ là một cột
                          mốc quan trọng trong hành trình học tập của chúng em,
                          mà còn là kết quả của những nỗ lực không ngừng nghỉ và
                          sự hỗ trợ từ nhiều phía. Chúng em vô cùng trân trọng
                          những trải nghiệm quý giá mà giai đoạn này mang lại.
                          Trước hết, chúng em xin gửi lời cảm ơn chân thành đến
                          ban giám hiệu nhà trường cùng toàn thể giảng viên
                          trong khoa Công nghệ thông tin, Trường Đại học Công
                          Thương TP. Hồ Chí Minh. Sự hướng dẫn và tạo điều kiện
                          từ thầy cô đã giúp chúng em vững bước trên con đường
                          học thuật. Chúng em đặc biệt muốn bày tỏ lòng biết ơn
                          đến thầy Vũ Văn Vinh, người đã trực tiếp hướng dẫn và
                          đồng hành cùng chúng em trong suốt quá trình thực hiện
                          khóa luận. Thầy đã dành nhiều thời gian và tâm huyết
                          để hỗ trợ, giúp chúng em vượt qua những thử thách và
                          hoàn thiện công trình nghiên cứu này. Chúng em nhận
                          thức rằng, trong quá trình thực hiện, không thể tránh
                          khỏi những thiếu sót. Do đó, chúng em rất mong nhận
                          được sự góp ý và hướng dẫn từ quý thầy cô và bạn bè để
                          có thể hoàn thiện hơn nữa trong tương lai. Cuối cùng,
                          chúng em xin cảm ơn gia đình và bạn bè đã luôn bên
                          cạnh, động viên và ủng hộ chúng em. Sự yêu thương và
                          tin tưởng của mọi người là nguồn động lực mạnh mẽ,
                          giúp chúng em tiến bước trên con đường học tập. Xin
                          chân thành cảm ơn !
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>

      <section id="tobias" class="tobias">
        <div class="container">
          <div class="row">
            <div class="main_tobias_area sections">
              <div class="col-sm-6">
                <div
                  class="single_abt single_tobias single_tobias_img wow fadeInLeft"
                  @mousemove="(event) => handleMouseMove(event, 0)"
                @mouseleave="() => resetZoom(0)"
                  ref="imageContainer"
                  style="position: relative; overflow: hidden"
                >
                  <img
                    src="../../assets/img/Transformer-Model.webp"
                    alt="Transformer Model"
                    ref="image"
                    :style="imageStyles[0]"
                    class="zoom-image"
                  />
                </div>
              </div>
              <div class="col-sm-5 col-sm-offset-1 black">
                <div
                  class="single_abt single_tobias single_tobias_text wow fadeInRight displayimg"
                >
                  <h4 class="text-uppercase">Mô tả</h4>
                  <div class="separator"></div>
                  <h3 class="text-uppercase">Mô hình phân loại văn bản</h3>
                  <h4 class="text-uppercase">BART + BERT</h4>
                  <p style="font-size: 20px">
                    Các nghiên cứu trước đây đã áp dụng nhiều phương pháp khác
                    nhau, bao gồm Collaborative Filtering, Content-Based
                    Filtering, và Hybrid Systems nhằm cá nhân hóa các đề xuất.
                    <mark>Phân loại bình luận</mark>(Comments Classification) là
                    một mảng quan trọng trong lĩnh vực
                    <mark>Natural Language Processing (NLP)</mark>, với mục tiêu
                    tự động phân loại các bình luận dựa trên cảm xúc, tính chất
                    tích cực/tiêu cực, hoặc nội dung phản hồi. Tuy nhiên, với sự
                    phát triển của các mô hình học máy và xử lý ngôn ngữ tự
                    nhiên (NLP), các hệ thống gợi ý và phân loại văn bản đang
                    ngày càng được cải tiến, đặc biệt với sự xuất hiện của các
                    mô hình tiên tiến như BART và BERT. Trong đề tài này, nhóm
                    nghiên cứu chúng tôi sử dụng các thuật toán hiện đại để xây
                    dựng một <mark>hệ thống gợi ý mentor cho mentee</mark>, nhằm
                    giảm thiểu các trường hợp matching mentor không phù hợp hoặc
                    xảy ra việc matching chéo giữa các mentor, và các vấn đề
                    liên quan khác xảy ra. Hệ thống cũng kết hợp với phân loại
                    và phân tích bình luận để ngăn chặn việc lợi dụng hệ sinh
                    thái mentoring cho những mục đích sai lệch, đảm bảo duy trì
                    tính chất lành mạnh và hiệu quả của quá trình mentoring
                    thông qua việc
                    <mark>lọc văn bản/ các mẫu câu bình luận</mark> tồn tại trên
                    hệ thống.
                  </p>
                </div>
              </div>
            </div>
            <!-- End of main Tobias area -->
          </div>
          <!-- End of row -->
        </div>
        <!-- End of container -->
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>
      <!-- End of Tobias Section -->

      <section id="service" class="service colorsbg">
        <div class="container">
          <div class="row">
            <div class="main_service_area text-center padding-bottom-80">
              <div class="head_title text-center wow fadeInUp">
                <h2>phân loại văn bản</h2>
                <p>Quy trình hoạt động được mô tả như minh họa bên dưới</p>
              </div>
              <div
                class="col-sm-offset-1"
                style="padding-bottom: 20px; margin-bottom: 20px"
              >
                <div class="single_abt single_about_right_img">
                  <img src="../../assets/img/Flowchart.png" alt="" />
                </div>
              </div>
              <div class="col-sm-4 wow fadeInLeft">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình marianMT để dịch thuật
                  </div>
                  <!-- <div class="service_btn">
                    <a href="" class="btn btn-larg">Mô hình <br> marianMT</a>
                  </div> -->
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInUp">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình BART để tóm tắt văn bản (giảm chiều dữ liệu
                    cho văn bản)
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInRight">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình BERT để phân loại văn bản
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->
            </div>

            <div class="row">
              <div
                class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
              >
                <div class="col-sm-3 no-padding">
                  <div
                    class="single_abt bottom_single_about bottom_single_about_left_img"
                  >
                    <img src="assets/images/a_b_left.jpg" alt="" />
                  </div>
                </div>
              </div>
            </div>

            <div class="main_service_area text-center padding-bottom-80">
              <div class="head_title text-center wow fadeInUp">
                <h2>gợi ý mentor phù hợp với mentee</h2>
                <p>Quy trình hoạt động được mô tả như minh họa bên dưới</p>
              </div>

              <div
                class="col-sm-offset-1"
                style="padding-bottom: 20px; margin-bottom: 20px"
              >
                <div
                  class="single_abt single_about_right_img"
                  @mousemove="handleMouseMove"
                  @mouseleave="resetZoom"
                  ref="imageContainer"
                  style="
                    position: relative;
                    overflow: hidden;
                    border-radius: 10px;
                  "
                >
                  <img
                    src="../../assets/img/Flowchart.svg"
                    alt="Flowchart"
                    ref="image"
                    :style="imageStyles"
                    class="zoom-image"
                    style="
                      height: 100%;
                      background-color: white;
                      height: 50vh;
                      border-radius: 10px;
                    "
                  />
                </div>
              </div>

              <div class="col-sm-4 wow fadeInLeft">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng cây K-ary để biểu diễn môí quan hệ các chuyên môn có
                    sẵn trong mô hình mentoring
                  </div>
                  <!-- <div class="service_btn">
                    <a href="" class="btn btn-larg">Mô hình <br> marianMT</a>
                  </div> -->
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInUp">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Matching dựa vào giới tính và chuyên môn của cả mentor và
                    mentee
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInRight">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">Xuất ra kết quả gợi ý</div>
                </div>
              </div>
              <!-- End of col-sm-4 -->
            </div>
            <!-- End of main service area -->
          </div>

          <!-- End of row -->
        </div>
      </section>

      <!-- End of Service Section -->

      <!-- Team Section -->
      <section id="team" class="team colorsbg">
        <div class="container">
          <div class="row">
            <div class="main_service_area main_team_area">
              <div class="head_title text-center wow fadeInUp">
                <h2>thành viên</h2>
              </div>

              <div class="main_team_content wow fadeInUp">
                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team1.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>Bùi xuân lộc</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team2.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>Vũ thị phương anh</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team3.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>trần thị bích hạnh</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->
              </div>
            </div>
            <!-- End of main Team area -->
          </div>
          <!-- End of row -->
        </div>
        <!-- End of container -->
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>
      <!-- End of Team Section -->

      <!-- Portfolio Section -->
      <section id="portfolio" class="colorsbg">
        <div class="container">
          <div class="row">
            <div class="maint_portfolio_area">
              <div class="col-sm-12">
                <div class="head_title margin-top-80 wow fadeInUp">
                  <h2>Quá trình làm việc</h2>
                  <p>
                    Truy cập vào đường link để xem quá trình nhóm đồ án thực
                    hiện
                  </p>
                  <a
                    href="https://docs.google.com/spreadsheets/d/1jc0haHPyHObegmGUL689tds3RaofLlZ7uJbN55yG-C8/edit?usp=sharing"
                    class="btn btn-default waves-effect waves-purple"
                    >Click vào đây</a
                  >
                </div>
              </div>

              <div class="main_portfolio_content sections wow fadeInUp">
                <div class="col-sm-8">
                  <div class="single_portfolio single_portfolio_1st">
                    <a href="assets/images/portfolio1.jpg" class="gallery-img"
                      ><img src="assets/images/portfolio1.jpg" alt=""
                    /></a>
                  </div>
                </div>
                <!-- End of col-sm-8 -->
                <div class="col-sm-4">
                  <div class="row">
                    <div class="col-sm-12">
                      <div class="single_portfolio">
                        <a
                          href="assets/images/portfolio2.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio2.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <div class="col-sm-12">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio3.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio3.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-12">
                  <div class="row">
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio4.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio4.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <!-- End of col-sm-4 -->
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio5.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio5.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <!-- End of col-sm-4 -->
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio6.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio6.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="wrapper tabled"
              style="padding-bottom: 20px; margin-bottom: 20px"
            >
              <div class="stage" id="page1">
                <div class="middled">
                  <h2>Demo sản phẩm</h2>
                  <h4>
                    Kết quả thực nghiệm cũng như demo dược hiển thị dưới đây.
                    <br />
                    <strong
                      >Vui lòng click vào đường link bên dưới để hiển thị thông
                      tin chi tiết</strong
                    >
                  </h4>
                  <div class="link-1">
                    <a
                      href="https://www.kaggle.com/code/buixuanloc/bart-summary-tweets"
                    >
                      <span class="thin">Mô hình</span><br /><span class="thick"
                        >BART</span
                      >
                    </a>
                    <p>
                      Đây là kết quả của nghiên cứu và fine tune mô hình tóm tắt
                      văn bản BART
                    </p>
                  </div>

                  <div class="link-2">
                    <a
                      href="https://www.kaggle.com/code/bixunlc/bert-classification-text"
                    >
                      <span class="thin">Mô hình</span><br /><span class="thick"
                        >BERT</span
                      >
                    </a>
                    <p>
                      Đây là kết quả nghiên cứu fine tune mô hình BERT để phân
                      loại văn bản
                    </p>
                  </div>

                  <div class="link-3">
                    <a
                      href="https://www.kaggle.com/code/buixuanloc/bart-bert-classification-text"
                    >
                      <span class="thin">Kết hợp</span><br /><span class="thick"
                        >BART + BERT</span
                      >
                    </a>
                    <p>Kết hợp 2 mô hình với nhau</p>
                  </div>

                  <div class="link-4">
                    <a
                      href="https://www.kaggle.com/models/buixuanloc/107-spensy-ai/"
                    >
                      <span class="thin">Xuất ra mô hình</span><br /><span
                        class="thick"
                        >BART + BERT</span
                      >
                    </a>
                    <p>Xuất ra mô hình và lưu trữ trên kaggle</p>
                  </div>

                  <div class="link-5">
                    <a href="https://www.kaggle.com/code/buixuanloc/used-bert">
                      <span class="thin">Ứng</span
                      ><span class="thick">Dụng</span>
                    </a>
                    <p>Thực nghiệm ứng dụng</p>
                  </div>

                  <!-- <div class="link-6">
                        <a href="#">
                          <span class="thin">link</span
                          ><span class="thick">six</span>
                        </a>
                        <p>minor scale up</p>
                      </div>

                      <div class="link-7">
                        <a href="#">
                          <span class="thin">link</span
                          ><span class="thick">seven</span>
                        </a>
                        <p>heartbeat</p>
                      </div> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </body>
</template>

<script>
export default {
  data() {
    return {
      zoomScale: 2, // Tỷ lệ phóng to (2x, 3x, ...)
      imageStyles: {
        transform: "scale(1)",
        transformOrigin: "center center",
        transition: "transform 0.2s ease-out",
      },
    };
  },
  methods: {
    handleMouseMove(event) {
      const container = this.$refs.imageContainer;
      // const image = this.$refs.image;

      // Lấy kích thước container và vị trí chuột
      const rect = container.getBoundingClientRect();
      const offsetX = event.clientX - rect.left;
      const offsetY = event.clientY - rect.top;

      // Tính vị trí tương đối của chuột theo % (giữa hình)
      const xPercent = (offsetX / rect.width) * 100;
      const yPercent = (offsetY / rect.height) * 100;

      // Cập nhật transform-origin và scale để phóng to
      this.imageStyles = {
        transform: `scale(${this.zoomScale})`,
        transformOrigin: `${xPercent}% ${yPercent}%`,
      };
    },
    resetZoom() {
      // Reset khi chuột rời khỏi ảnh
      this.imageStyles = {
        transform: "scale(1)",
        transformOrigin: "center center",
      };
    },
  },
};
</script>

<template>
  <body data-spy="scroll" data-target="#scrollspy">
    <div class="main_figur">
      <section id="about" class="about colorsbg">
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-12">
              <div class="main_about_area">
                <div class="head_title text-center">
                  <h2>Giới thiệu</h2>
                </div>
                <div
                  class="about_content colorstext2 wow fadeInUp"
                  data-wow-duration="700ms"
                >
                  <div class="row">
                    <div class="col-sm-9 col-sm-offset-1">
                      <div class="single_abt single_about">
                        <h3>107 SPENSY</h3>
                        <p class="text-uppercase colorstext">LỜI CẢM ƠN</p>
                        <p class="special_thanks">
                          Hoàn thành khóa luận tốt nghiệp không chỉ là một cột
                          mốc quan trọng trong hành trình học tập của chúng em,
                          mà còn là kết quả của những nỗ lực không ngừng nghỉ và
                          sự hỗ trợ từ nhiều phía. Chúng em vô cùng trân trọng
                          những trải nghiệm quý giá mà giai đoạn này mang lại.
                          Trước hết, chúng em xin gửi lời cảm ơn chân thành đến
                          ban giám hiệu nhà trường cùng toàn thể giảng viên
                          trong khoa Công nghệ thông tin, Trường Đại học Công
                          Thương TP. Hồ Chí Minh. Sự hướng dẫn và tạo điều kiện
                          từ thầy cô đã giúp chúng em vững bước trên con đường
                          học thuật. Chúng em đặc biệt muốn bày tỏ lòng biết ơn
                          đến thầy Vũ Văn Vinh, người đã trực tiếp hướng dẫn và
                          đồng hành cùng chúng em trong suốt quá trình thực hiện
                          khóa luận. Thầy đã dành nhiều thời gian và tâm huyết
                          để hỗ trợ, giúp chúng em vượt qua những thử thách và
                          hoàn thiện công trình nghiên cứu này. Chúng em nhận
                          thức rằng, trong quá trình thực hiện, không thể tránh
                          khỏi những thiếu sót. Do đó, chúng em rất mong nhận
                          được sự góp ý và hướng dẫn từ quý thầy cô và bạn bè để
                          có thể hoàn thiện hơn nữa trong tương lai. Cuối cùng,
                          chúng em xin cảm ơn gia đình và bạn bè đã luôn bên
                          cạnh, động viên và ủng hộ chúng em. Sự yêu thương và
                          tin tưởng của mọi người là nguồn động lực mạnh mẽ,
                          giúp chúng em tiến bước trên con đường học tập. Xin
                          chân thành cảm ơn !
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>

      <section id="tobias" class="tobias">
        <div class="container">
          <div class="row">
            <div class="main_tobias_area sections">
    <div
      class="col-sm-6"
      @mousemove="(event) => handleMouseMove(event, 0)"
      @mouseleave="() => resetZoom(0)"
      ref="imageContainer1"
      style="position: relative; overflow: hidden; margin-bottom: 20px;"
    >
      <img
        src="../../assets/img/Transformer-Model.webp"
        alt="Transformer Model"
        ref="image1"
        :style="imageStyles[0]"
        class="zoom-image"
        style="height: 100%;"
      />
    </div>

              <div class="col-sm-5 col-sm-offset-1 black">
                <div
                  class="single_abt single_tobias single_tobias_text wow fadeInRight displayimg"
                >
                  <h4 class="text-uppercase">Mô tả</h4>
                  <div class="separator"></div>
                  <h3 class="text-uppercase">Mô hình phân loại văn bản</h3>
                  <h4 class="text-uppercase">BART + BERT</h4>
                  <p style="font-size: 20px">
                    Các nghiên cứu trước đây đã áp dụng nhiều phương pháp khác
                    nhau, bao gồm Collaborative Filtering, Content-Based
                    Filtering, và Hybrid Systems nhằm cá nhân hóa các đề xuất.
                    <mark>Phân loại bình luận</mark>(Comments Classification) là
                    một mảng quan trọng trong lĩnh vực
                    <mark>Natural Language Processing (NLP)</mark>, với mục tiêu
                    tự động phân loại các bình luận dựa trên cảm xúc, tính chất
                    tích cực/tiêu cực, hoặc nội dung phản hồi. Tuy nhiên, với sự
                    phát triển của các mô hình học máy và xử lý ngôn ngữ tự
                    nhiên (NLP), các hệ thống gợi ý và phân loại văn bản đang
                    ngày càng được cải tiến, đặc biệt với sự xuất hiện của các
                    mô hình tiên tiến như BART và BERT. Trong đề tài này, nhóm
                    nghiên cứu chúng tôi sử dụng các thuật toán hiện đại để xây
                    dựng một <mark>hệ thống gợi ý mentor cho mentee</mark>, nhằm
                    giảm thiểu các trường hợp matching mentor không phù hợp hoặc
                    xảy ra việc matching chéo giữa các mentor, và các vấn đề
                    liên quan khác xảy ra. Hệ thống cũng kết hợp với phân loại
                    và phân tích bình luận để ngăn chặn việc lợi dụng hệ sinh
                    thái mentoring cho những mục đích sai lệch, đảm bảo duy trì
                    tính chất lành mạnh và hiệu quả của quá trình mentoring
                    thông qua việc
                    <mark>lọc văn bản/ các mẫu câu bình luận</mark> tồn tại trên
                    hệ thống.
                  </p>
                </div>
              </div>
            </div>
            <!-- End of main Tobias area -->
          </div>
          <!-- End of row -->
        </div>
        <!-- End of container -->
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>
      <!-- End of Tobias Section -->

      <section id="service" class="service colorsbg">
        <div class="container">
          <div class="row">
            <div class="main_service_area text-center padding-bottom-80">
              <div class="head_title text-center wow fadeInUp">
                <h2>phân loại văn bản</h2>
                <p>Quy trình hoạt động được mô tả như minh họa bên dưới</p>
              </div>
              <div
                class="col-sm-offset-1"
                style="padding-bottom: 20px; margin-bottom: 20px"
              >
                <div class="single_abt single_about_right_img">
                  <img src="../../assets/img/Flowchart.png" alt="" />
                </div>
              </div>
              <div class="col-sm-4 wow fadeInLeft">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình marianMT để dịch thuật
                  </div>
                  <!-- <div class="service_btn">
                    <a href="" class="btn btn-larg">Mô hình <br> marianMT</a>
                  </div> -->
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInUp">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình BART để tóm tắt văn bản (giảm chiều dữ liệu
                    cho văn bản)
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInRight">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng mô hình BERT để phân loại văn bản
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->
            </div>

            <div class="row">
              <div
                class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
              >
                <div class="col-sm-3 no-padding">
                  <div
                    class="single_abt bottom_single_about bottom_single_about_left_img"
                  >
                    <img src="assets/images/a_b_left.jpg" alt="" />
                  </div>
                </div>
              </div>
            </div>

            <div class="main_service_area text-center padding-bottom-80">
              <div class="head_title text-center wow fadeInUp">
                <h2>gợi ý mentor phù hợp với mentee</h2>
                <p>Quy trình hoạt động được mô tả như minh họa bên dưới</p>
              </div>

              <div
                class="col-sm-offset-1"
                style="padding-bottom: 20px; margin-bottom: 20px"
              >
 <div
      class="col-sm-offset-1"
      @mousemove="(event) => handleMouseMove(event, 1)"
      @mouseleave="() => resetZoom(1)"
      ref="imageContainer2"
      style="position: relative; overflow: hidden; border-radius: 10px; margin-bottom: 20px;"
    >
      <img
        src="../../assets/img/Flowchart.svg"
        alt="Flowchart"
        ref="image2"
        :style="imageStyles[1]"
        class="zoom-image"
        style="
          height: 100%;
          background-color: white;
          height: 50vh;
          border-radius: 10px;
        "
      />
    </div>
              </div>

              <div class="col-sm-4 wow fadeInLeft">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Sử dụng cây K-ary để biểu diễn môí quan hệ các chuyên môn có
                    sẵn trong mô hình mentoring
                  </div>
                  <!-- <div class="service_btn">
                    <a href="" class="btn btn-larg">Mô hình <br> marianMT</a>
                  </div> -->
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInUp">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">
                    Matching dựa vào giới tính và chuyên môn của cả mentor và
                    mentee
                  </div>
                </div>
              </div>
              <!-- End of col-sm-4 -->

              <div class="col-sm-4 wow fadeInRight">
                <div class="single_service margin-top-40">
                  <div class="single_service_img">Xuất ra kết quả gợi ý</div>
                </div>
              </div>
              <!-- End of col-sm-4 -->
            </div>
            <!-- End of main service area -->
          </div>

          <!-- End of row -->
        </div>
      </section>

      <!-- End of Service Section -->

      <!-- Team Section -->
      <section id="team" class="team colorsbg">
        <div class="container">
          <div class="row">
            <div class="main_service_area main_team_area">
              <div class="head_title text-center wow fadeInUp">
                <h2>thành viên</h2>
              </div>

              <div class="main_team_content wow fadeInUp">
                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team1.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>Bùi xuân lộc</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team2.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>Vũ thị phương anh</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-4 col-xs-12">
                  <div class="single_team margin-top-40">
                    <img src="assets/images/team3.jpg" alt="" />
                    <div class="single_team_text">
                      <h4><strong>trần thị bích hạnh</strong></h4>
                      <p>MSSV: <strong>2001215927</strong></p>
                      <p>Lớp: <strong>12DHTH16</strong></p>
                      <p>Chuyên ngành: <strong>Khoa học dữ liệu</strong></p>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->
              </div>
            </div>
            <!-- End of main Team area -->
          </div>
          <!-- End of row -->
        </div>
        <!-- End of container -->
        <div class="container">
          <div class="row">
            <div
              class="about_bottom colorstext margin-top-80 margin-bottom-80 wow fadeInUp"
            >
              <div class="col-sm-3 no-padding">
                <div
                  class="single_abt bottom_single_about bottom_single_about_left_img"
                >
                  <img src="assets/images/a_b_left.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
          <!-- End of row -->
        </div>
      </section>
      <!-- End of Team Section -->

      <!-- Portfolio Section -->
      <section id="portfolio" class="colorsbg">
        <div class="container">
          <div class="row">
            <div class="maint_portfolio_area">
              <div class="col-sm-12">
                <div class="head_title margin-top-80 wow fadeInUp">
                  <h2>Quá trình làm việc</h2>
                  <p>
                    Truy cập vào đường link để xem quá trình nhóm đồ án thực
                    hiện
                  </p>
                  <a
                    href="https://docs.google.com/spreadsheets/d/1jc0haHPyHObegmGUL689tds3RaofLlZ7uJbN55yG-C8/edit?usp=sharing"
                    class="btn btn-default waves-effect waves-purple"
                    >Click vào đây</a
                  >
                </div>
              </div>

              <div class="main_portfolio_content sections wow fadeInUp">
                <div class="col-sm-8">
                  <div class="single_portfolio single_portfolio_1st">
                    <a href="assets/images/portfolio1.jpg" class="gallery-img"
                      ><img src="assets/images/portfolio1.jpg" alt=""
                    /></a>
                  </div>
                </div>
                <!-- End of col-sm-8 -->
                <div class="col-sm-4">
                  <div class="row">
                    <div class="col-sm-12">
                      <div class="single_portfolio">
                        <a
                          href="assets/images/portfolio2.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio2.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <div class="col-sm-12">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio3.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio3.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End of col-sm-4 -->

                <div class="col-sm-12">
                  <div class="row">
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio4.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio4.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <!-- End of col-sm-4 -->
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio5.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio5.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                    <!-- End of col-sm-4 -->
                    <div class="col-sm-4">
                      <div class="single_portfolio margin-top-30">
                        <a
                          href="assets/images/portfolio6.jpg"
                          class="gallery-img"
                          ><img src="assets/images/portfolio6.jpg" alt=""
                        /></a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="wrapper tabled"
              style="padding-bottom: 20px; margin-bottom: 20px"
            >
              <div class="stage" id="page1">
                <div class="middled">
                  <h2>Demo sản phẩm</h2>
                  <h4>
                    Kết quả thực nghiệm cũng như demo dược hiển thị dưới đây.
                    <br />
                    <strong
                      >Vui lòng click vào đường link bên dưới để hiển thị thông
                      tin chi tiết</strong
                    >
                  </h4>
                  <div class="link-1">
                    <a
                      href="https://www.kaggle.com/code/buixuanloc/bart-summary-tweets"
                    >
                      <span class="thin">Mô hình</span><br /><span class="thick"
                        >BART</span
                      >
                    </a>
                    <p>
                      Đây là kết quả của nghiên cứu và fine tune mô hình tóm tắt
                      văn bản BART
                    </p>
                  </div>

                  <div class="link-2">
                    <a
                      href="https://www.kaggle.com/code/bixunlc/bert-classification-text"
                    >
                      <span class="thin">Mô hình</span><br /><span class="thick"
                        >BERT</span
                      >
                    </a>
                    <p>
                      Đây là kết quả nghiên cứu fine tune mô hình BERT để phân
                      loại văn bản
                    </p>
                  </div>

                  <div class="link-3">
                    <a
                      href="https://www.kaggle.com/code/buixuanloc/bart-bert-classification-text"
                    >
                      <span class="thin">Kết hợp</span><br /><span class="thick"
                        >BART + BERT</span
                      >
                    </a>
                    <p>Kết hợp 2 mô hình với nhau</p>
                  </div>

                  <div class="link-4">
                    <a
                      href="https://www.kaggle.com/models/buixuanloc/107-spensy-ai/"
                    >
                      <span class="thin">Xuất ra mô hình</span><br /><span
                        class="thick"
                        >BART + BERT</span
                      >
                    </a>
                    <p>Xuất ra mô hình và lưu trữ trên kaggle</p>
                  </div>

                  <div class="link-5">
                    <a href="https://www.kaggle.com/code/buixuanloc/used-bert">
                      <span class="thin">Ứng</span
                      ><span class="thick">Dụng</span>
                    </a>
                    <p>Thực nghiệm ứng dụng</p>
                  </div>

                  <!-- <div class="link-6">
                        <a href="#">
                          <span class="thin">link</span
                          ><span class="thick">six</span>
                        </a>
                        <p>minor scale up</p>
                      </div>

                      <div class="link-7">
                        <a href="#">
                          <span class="thin">link</span
                          ><span class="thick">seven</span>
                        </a>
                        <p>heartbeat</p>
                      </div> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </body>
</template>

