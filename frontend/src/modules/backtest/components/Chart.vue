<template>
<div class="">
    <view id="MyChart"  class="k-line-chart" style="height: 600px"></view>
  </div>
</template>
<script>
import { init } from 'klinecharts'
export default {
  name: 'ChartTypeKLineChart',
  data: function () {
    return {
      chartTypes: [
        { key: 'candle_solid', text: '蜡烛实心' },
        { key: 'candle_stroke', text: '蜡烛空心' },
        { key: 'candle_up_stroke', text: '蜡烛涨空心' },
        { key: 'candle_down_stroke', text: '蜡烛跌空心' },
        { key: 'ohlc', text: 'OHLC' },
        { key: 'area', text: '面积图' }
      ]
    }
  },
  mounted: function () {
    this.kLineChart = init('chart-type-k-line')
    this.kLineChart.applyNewData(this.generatedKLineDataList)
  },
  methods: {
    setChartType: function (type) {
      this.kLineChart.setStyleOptions({
        candle: {
          type
        }
      })
    },
    generatedKLineDataList: function (baseTimestamp = Date.now(), basePrice = 5000, dataSize = 800) {
  const dataList = []
  let timestamp = Math.floor(baseTimestamp / 60 / 1000) * 60 * 1000
  let baseValue = basePrice
  const prices = []
  for (let i = 0; i < dataSize; i++) {
    baseValue = baseValue + Math.random() * 20 - 10
    for (let j = 0; j < 4; j++) {
      prices[j] = (Math.random() - 0.5) * 12 + baseValue
    }
    prices.sort()
    const openIdx = +Math.round(Math.random() * 3).toFixed(0)
    let closeIdx = +Math.round(Math.random() * 2).toFixed(0)
    if (closeIdx === openIdx) {
      closeIdx++
    }
    const volume = Math.random() * 50 + 10
    const kLineModel = {
      open: prices[openIdx],
      low: prices[0],
      high: prices[3],
      close: prices[closeIdx],
      volume: volume,
      timestamp
    }
    timestamp -= 60 * 1000
    kLineModel.turnover = (kLineModel.open + kLineModel.close + kLineModel.high + kLineModel.low) / 4 * volume
    dataList.unshift(kLineModel)
  }
  return dataList
}
  },

}

</script>