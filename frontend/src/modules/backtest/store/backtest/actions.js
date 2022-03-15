import backtestAPI from "@/api/backtestAPI"


/* 
export const myAction = async ({ commit }) => {

}
 */


export const updateListIndicators = async ({ commit }, indicators ) => {
    commit("updateListIndicators", indicators)
}

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


export const deleteIndicator = ({ commit }, id ) => {

    commit("deleteIndicator", id )

    return { ok: true }
}


export const startBacktest = async ({ commit, state }, tickerData ) => {

    commit("loading")

    const indicator = state.indicators

    const indicatorsData = []

    indicator.forEach(element => {
        indicatorsData.push({...element})
    })

    const dataBacktest = { ...tickerData, indicatorsData }

    try {
        const { data } = await backtestAPI.post('/backtest/', dataBacktest)
        commit("setBacktest", data.data)
        commit("loading")
        return { ok: true, message: data.message }
        
    } catch (error) {
        commit("loading")
        return { ok: false, message: error }   
    }
}

