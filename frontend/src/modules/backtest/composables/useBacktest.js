import { computed } from "vue"
import { useStore } from "vuex"

const useBacktest = () => {

    const store = useStore()

    const addIndicator = ( indicator ) => {
        
        store.dispatch("backtest/addIndicator", indicator)
    }

    return {
        addIndicator,
    }

}