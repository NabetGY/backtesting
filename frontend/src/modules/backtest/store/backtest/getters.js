
/* export const myGetters = ( state ) => {
    return state
} */


export const getPositionIndicator = ( state ) => ( name='' ) => {
    console.log(name)
    return state.indicators.findIndex(indicator => indicator.indicatorName === name )
}

const toTimestamp = (strDate) => {  
    const dt = new Date(strDate).getTime();  
    return dt / 1000;  
  }

export const getMarkets = ( state ) => {
    const { report } = state.backtests[0]
    const lista = []
    for (const item of report.data) {
        if (item[0]==1) {
            lista.push({time: toTimestamp(item[1]), position: 'belowBar', color: '#2196F3', shape: 'arrowUp', text: 'Buy ' + [2]})
        } else {
            lista.push({time: toTimestamp(item[1]), position: 'aboveBar', color: '#e91e63', shape: 'arrowDown', text: 'Sell ' + [3]})
        }
    }
    console.log(lista)
    return lista
}