/* 
export const myMutations = ( state ) => {

}
 */

export const setTickers = ( state, tickers ) => {

    state.tickers = [ ...state.tickers, ...tickers]
    state.isLoading = false

}

export const setIndicator = ( state, indicator ) => {

    state.indicators = [ ...state.indicators, indicator]
}


export const setBacktest = ( state, backtest ) => {

    state.backtests = [ backtest, ...state.backtests ]
}

export const updateListIndicators = ( state, indicators ) => {
    state.indicators = indicators
}