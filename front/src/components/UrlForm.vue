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
                  type="url"
                  placeholder="https://www.example.com"
                  class="form-control form-control-lg"
                  autocomplete="off"
                  id="input_url"
                  name="input_url"
                  v-model.trim="input_url"
                  aria-describedby="input_url_help"
                  @blur="validateInput"
                />
                <div v-if="is_invalid" class="text-danger">
                  Url must be provided
                </div>
                <div v-else-if="is_valid_url" class="text-danger">
                  The url is invalid
                </div>
              </div>
              <button type="submit" class="btn btn-primary">
                Generate Short Url
              </button>
            </div>
          </div>
        </div>
        <div class="col-8 offset-2 mt-3">
          <div v-if="short_url" class="card">
            <div class="card-body">
              <div class="mb-3">
                <label for="shor_url" class="form-label">Short Url</label>
                <input
                  type="text"
                  class="form-control form-control-lg"
                  autocomplete="off"
                  id="shor_url"
                  name="shor_url"
                  :value="short_url"
                  aria-describedby="shor_url_help"
                />
              </div>
              <p>
                <a :href="short_url" class="btn btn-outline-dark">Visit</a>
              </p>
            </div>
          </div>
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
      short_url: "",
      is_invalid: false,
      is_valid_url: false,
      valid_url: /^(ftp|http|https):\/\/[^ "]+$/,
    };
  },
  methods: {
    validateInput() {
      if (this.input_url == "") {
        this.is_invalid = !this.is_invalid;
      } else {
        if (!this.valid_url.test(this.input_url)) {
          this.is_valid_url = !this.is_valid_url;
        }
      }
    },
    submitForm() {
      this.validateInput();
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      const userData = {
        long_url: this.input_url,
      };

      let requestOptions = {
        method: "POST",
        body: JSON.stringify(userData),
        headers: headers,
      };

      const url = "http://localhost:8000/create/";
      fetch(url, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          this.short_url = response.short_url;
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
