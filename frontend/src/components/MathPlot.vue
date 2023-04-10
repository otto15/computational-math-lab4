<template>
  <div ref="plot"/>
</template>

<script>
import Plotly from 'plotly.js-dist';

export default {
  props: {
    func: {
      type: String,
      required: true,
      default: "x"
    },
    range: {
      type: Array,
      default: () => [-10, 10]
    },
    numPoints: {
      type: Number,
      default: 100
    }
  },
  watch: {
    func: 'renderPlot'
  },
  mounted() {
    this.renderPlot();
  },
  methods: {
    renderPlot() {
      const {func, range, numPoints} = this;

      const xs = [];
      const ys = [];
      const step = (range[1] - range[0]) / numPoints;

      for (let x = range[0]; x <= range[1]; x += step) {
        xs.push(x);
        ys.push(eval(func));
      }

      const trace = {
        x: xs,
        y: ys
      };

      const layout = {
        xaxis: {
          title: 'x'
        },
        yaxis: {
          title: 'y'
        }
      };

      Plotly.newPlot(this.$refs.plot, [trace], layout);
    }
  }
};
</script>

<style scoped>
div {
  width: 100%;
  height: 100%;
}
</style>
