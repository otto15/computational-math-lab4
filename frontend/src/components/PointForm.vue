<template>
  <div class="container">
    <div class="tb">
      <table class="points-table">
        <thead>
        <tr>
          <th>X</th>
          <th>Y</th>
          <th></th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(point, index) in points" :key="index">
          <td>
            <input type="number" v-model.number="point.x" step="0.01" :ref="`x${index}`">
          </td>
          <td>
            <input type="number" v-model.number="point.y" step="0.01" :ref="`y${index}`">
          </td>
          <td>
            <button @click="removePoint(index)" class="remove-btn">Remove</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div class="buttons-container">
      <button @click="addPoint" :disabled="points.length >= 12" class="add-btn">Add Point</button>
      <button @click="sendPoints" :disabled="!isValid || points.length < 8 || points.length > 12" class="send-btn">
        Approximate
      </button>
    </div>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      points: [{x: null, y: null}],
      errorMessage: null,
    };
  },
  mounted() {
    this.focusLastX();
  },
  computed: {
    isValid() {
      let only_x = this.points.map(point => point.x)
      let st = new Set(only_x)
      if (st.size !== only_x.length) return false
      return this.points.every(point => point.x !== null && point.y !== null && point.x !== "" && point.y !== "");
    },
  },
  methods: {
    addPoint() {
      if (this.points.length < 12) {
        this.points.push({x: null, y: null});
        this.$nextTick(() => {
          this.focusLastX();
        });
      }
    },
    removePoint(index) {
      this.points.splice(index, 1);
    },
    sendPoints() {
      if (this.isValid) {
        axios
            .post('http://localhost:8000/approximation', {points: this.points})
            .then(response => {
              console.log(response.data);
              this.$emit('approximation-result', response.data);
            })
            .catch(() => {
              this.errorMessage = 'Error sending points to server';
            });
      } else {
        this.errorMessage = 'Invalid point values';
      }
    },
    focusLastX() {
      const lastIndex = this.points.length - 1;

      let xInput = this.$refs[`x${lastIndex}`][0];
      let yInput = this.$refs[`y${lastIndex}`][0];
      xInput.focus();

      xInput.addEventListener('keydown', (event) => {
        if (event.key !== 'Enter') return;
        if (xInput.value !== '') {
          yInput.focus();
        }
      });
    }
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}

.points-table {
  border-style: hidden;
  border-collapse: collapse;
  width: 100%;
}

.tb {
  border: 2px solid #ccc;
  border-radius: 10px;
}

.points-table th,
.points-table td {
  font-family: Arial, serif;
  padding: 0.5rem;
  text-align: center;
  border: 2px solid #ccc;
}

.points-table th:first-child {
  border-radius: 10px 0 0 0;
}

.points-table th:last-child {
  border-radius: 0 10px 0 0;
}

.points-table th {
  background-color: #f5f5f5;
}

.points-table tr:last-child td:first-child {
  border-radius: 0 0 0 10px;
}

.points-table tr:last-child td:last-child {
  border-radius: 0 0 10px 0;
}

.points-table input[type="number"] {
  font-family: Arial, serif;
  width: 80%;
  padding: 0.5rem;
  border: none;
  text-align: center;
  font-size: 15px;
}

.buttons-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.add-btn,
.send-btn,
.remove-btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  font-size: 1rem;
  font-weight: bold;
  color: #fff;
  background-color: #4caf50;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.add-btn:disabled,
.send-btn:disabled {
  opacity: 0.5;
  cursor: default;
}

.send-btn {
  background-color: #2196f3;
}

.remove-btn {
  background-color: #f44336;
}

.add-btn:hover {
  background-color: #3e8e41;
}

.send-btn:hover {
  background-color: #0673c0;
}

.remove-btn:hover {
  background-color: #b21e13;
}

.error-message {
  margin-top: 1rem;
  padding: 0.5rem;
  border: 1px solid #f44336;
  background-color: #ffebee;
  color: #f44336;
  font-size: 0.8rem;
  text-align: center;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  /* display: none; <- Crashes Chrome on hover */
  -webkit-appearance: none;
  margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}
</style>