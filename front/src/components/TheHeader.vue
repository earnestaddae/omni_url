<template>
  <!-- Example Code -->

  <nav class="navbar navbar-expand-lg bg-flight p-3">
    <div class="container">
      <router-link to="/" class="navbar-brand fw-bold text-uppercase fs-5"
        ><span id="brand-name">Omnihr</span>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
  </nav>

  <!-- End Example Code -->
</template>
  
  
  <style scoped>
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@700&display=swap");
.bg-flight {
  color: #fff !important;
  background-color: #6161b5 !important;
  /* background-color: RGBA(0,128,128,var(--bs-bg-opacity, 1))!important; */
  /* background-color: RGBA(28,169,201,var(--bs-bg-opacity, 1))!important;#206c5f #053129 */
}
#brand-name {
  font-family: "Quicksand", sans-serif;
  font-weight: 700;
  letter-spacing: 0.25rem;
  line-height: 100%;
  display: inline-block;
  color: #fff;
  /* border: 2px solid #053129; */
  padding-top: 3px;
  border-left: none;
  border-right: none;
  text-shadow: 2px 8px 6px rgba(0, 0, 0, 0.2),
    0px -5px 35px rgba(255, 255, 255, 0.3);
}
</style>
  