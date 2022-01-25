import backtestAPI from "@/api/backtestAPI"


/* 
export const myAction = async ({ commit }) => {

}
 */

export const loadTickers = async ( { commit } ) => {

    const { data } = await backtestAPI.get('/tickers/ticker.json')
    const tickers = []
    for( let id of Object.keys( data )) {
        tickers.push({
            id,
            ...data[id]
        })
        
    }
    commit('setTickers', tickers)
}


export const addIndicator = ({ commit }, indicator ) => {

    const dataToSave = {...indicator}

    commit("setIndicator", dataToSave)
}


export const startBacktest = async ({ /* commit, */ state }, tickerData ) => {

    const indicator = state.indicators

    const indicatorsData = []

    indicator.forEach(element => {
        indicatorsData.push({...element})
    })

    const dataBacktest = {...tickerData, indicatorsData}

    const { data } = await backtestAPI.post('/backtest/', dataBacktest)

    console.log(data)


    /* commit("setTickerData", tickerData) */
}

/* export default startBacktest =  ({ commit }, tickerData) => {

    

} */