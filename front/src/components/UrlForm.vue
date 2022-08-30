<template>
  <div class="container mt-5">
    <form
      class="row g-3 needs-validation"
      novalidate
      @submit.prevent="submitForm"
    >
      <div class="row">
        <div class="col-8 offset-2">
          <div class="card">
            <div class="card-body">
              <div class="mb-3">
                <label for="input_url" class="form-label">Enter long url</label>
                <input
                  type="text"
                  class="form-control form-control-lg"
                  autocomplete="off"
                  id="input_url"
                  name="input_url"
                  v-model.trim="input_url"
                  aria-describedby="input_url_help"
                  required
                />
                <div class="invalid-feedback">Url must be provided.</div>
              </div>

              <button type="submit" class="btn btn-primary">
                Generate Short Url
              </button>
            </div>
          </div>
        </div>
        <div class="col-8 offset-2 mt-3">
          <h2>Short Url</h2>
          <p>{{ input_url }}</p>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "UrlForm",
  data() {
    return {
      input_url: "",
    };
  },
  methods: {
    submitForm() {
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const userData = {
        input_url: this.input_url,
      };

      let requestOptions = {
        method: "POST",
        body: JSON.stringify(userData),
        headers: headers,
      };

      const url = "http://localhost:8000/api/urlshortener/create";
      fetch(url, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
label {
  font-size: 1.25rem;
  font-weight: bold;
}
input,
textarea {
  background-color: #f3f6f6 !important;
}
</style>
