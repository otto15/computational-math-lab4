<script setup>
import PointForm from "@/components/PointForm.vue";
import MathPlot from "@/components/MathPlot.vue";
</script>

<template>
  <header>
    <h1>Computational Lab #4</h1>
  </header>
  <main>
    <PointForm @approximation-result="handleApproximationResult"/>
    <div v-if="result !== null" class="result-block">
      <h2>Result:</h2>
      <p class="result">g(x) = {{ phi }}</p>
    </div>
    <div v-if="result !== null" class="plots">
      <div v-if="cubic !== null" class="plot">
        <MathPlot :func="cubic"/>
        <div class="plot-title">f(x) = {{ cubic }}</div>
      </div>
      <div v-if="exp !== null" class="plot">
        <MathPlot :func="exp"/>
        <div class="plot-title">f(x) = {{ exp }}</div>
      </div>
      <div v-if="log !== null" class="plot">
        <MathPlot :func="log"/>
        <div class="plot-title">f(x) = {{ log }}</div>
      </div>
      <div v-if="linear !== null" class="plot">
        <MathPlot :func="linear"/>
        <div class="plot-title">f(x) = {{ linear }}</div>
      </div>
      <div v-if="square !== null"  class="plot">
        <MathPlot :func="square"/>
        <div class="plot-title">f(x) = {{ square }}</div>
      </div>
      <div v-if="power !== null" class="plot">
        <MathPlot :func="power"/>
        <div class="plot-title">f(x) = {{ power }}</div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      result: null,
      phi: null,
      empiric_functions: new Map(),
      cubic: null,
      log: null,
      exp: null,
      linear: null,
      power: null,
      square: null
    }
  },
  methods: {
    handleApproximationResult(result) {
      this.empiric_functions = new Map([
        ['log', result['log'].length === 0 ? null : `${result['log'][0]} + Math.log(x) * ${result['log'][1]}`],
        ['cubic', result.cubic.length === 0 ? null : `${result.cubic[0]} + ${result.cubic[1]} * x + ${result.cubic[2]} * (x)**2 + ${result.cubic[3]} * (x)**3`],
        ['exp', result['exp'].length === 0 ? null : `${result['exp'][1]} + Math.exp(${result['exp'][0]}*(x))`],
        ['linear', result.linear.length === 0 ? null : `${result.linear[0]} + ${result.linear[1]}*(x)`],
        ['power', result.power.length === 0 ? null : `${result.power[1]} * (x)**${result.power[0]}`],
        ['square', result.square.length === 0 ? null : `${result.cubic[0]} + ${result.cubic[1]} * x + ${result.cubic[2]} * (x)**2`],
      ]);

      this.phi = this.empiric_functions.get(result.chosen)
      this.cubic = this.empiric_functions.get('cubic')
      this.log = this.empiric_functions.get('log')
      this.exp = this.empiric_functions.get('exp')
      this.linear = this.empiric_functions.get('linear')
      this.power = this.empiric_functions.get('power')
      this.square = this.empiric_functions.get('square')

      this.result = result;
    }
  },
}
</script>

<style scoped>
header {
  font-family: Montserrat, sans-serif;
  color: black;
  padding: 20px;
  text-align: center;
}

header h1 {
  margin: 0;
}

.plots {
  width: 80%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  margin-left: auto;
  margin-right: auto;
}

.plot {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 400px;
  height: 300px;
  border: 1px solid #ddd;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  padding: 10px;
}

.plot canvas {
  width: 100%;
  height: 80%;
}

.plot-title {
  font-family: Montserrat, sans-serif;
  font-size: 0.8rem;
  font-weight: bold;
  margin-top: 10px;
}

.result-block {
  width: 50%;
  font-family: Montserrat, sans-serif;
  font-size: 1.0rem;
  font-weight: bold;
  margin: 0 auto;
  text-align: center;
}
</style>
