<template>
  <div class="modall-backdrop">
    <div class="modall">
      <b-container class="mt-3 mb-3">
        <div class="modal__input">
          <b-row>
            <b-col>
              <b-button @click="$emit('close')" class="float-right mx-2">
                <b-icon icon="x-circle"></b-icon>
              </b-button>
            </b-col>
          </b-row>
        </div>

        <div class="modal__input">
          <b-row>
            <div>
              <span>Name: </span>
            </div>
            <div>
              <b-form-input type="text" v-model="name"></b-form-input>
            </div>
          </b-row>
        </div>

        <div class="modal__input">
          <b-row>
            <div><span>Address: </span></div>
            <div>
              <b-form-input type="text" v-model="address"></b-form-input>
            </div>
          </b-row>
        </div>

        <div class="modal__input">
          <b-row>
            <div><span>Phone number: </span></div>
            <div>
              <b-form-input type="text" v-model="phone_number"></b-form-input>
            </div>
          </b-row>
        </div>

        <div class="modal__input">
          <b-row>
            <p>Total price: {{ pay_total }}$</p>
          </b-row>
        </div>
        <div>
          <b-row class="btn">
            <b-button @click="sendOrder">Xác nhận</b-button>
          </b-row>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    pay_total: String,
  },
  data() {
    return {
      name: "",
      address: "",
      phone_number: "",
    };
  },
  methods: {
    sendOrder() {
      axios
        .post("http://localhost:8000/api/foodorders/", {
          price: this.pay_total,
          name: this.name,
          address: this.address,
          phone_number: this.phone_number,
          food: [],
        })
        .then((respone) => console.log(respone))
        .catch((err) => alert(err));

      this.name = this.address = this.phone_number = "";
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.modal__input + .modal__input {
  margin-bottom: 1rem !important;
  margin-left: 2rem !important;
}
p {
  font-size: 1.3rem;
}
.btn {
  margin-left: 1rem !important;
}
span {
  margin-right: .5rem;
}
</style>
