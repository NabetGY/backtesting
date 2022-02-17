<template>
    <table class="table table-striped table-hover">
        <thead>
            <tr >
                <th scope="col">#</th>
                <th scope="col">In/Out</th>
                <th scope="col">Date</th>
                <th scope="col">Price in</th>
                <th scope="col">STP</th>
                <th scope="col">STP %</th>
                <th scope="col">Positions</th>
                <th scope="col">TGT</th>
                <th scope="col">Price out</th>
                <th scope="col">Profit Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in report.data" :key="item.id">
                <th scope="row">{{ index+1 }}</th>
                <td v-if="item[0]===-1">
                    <i class="bi bi-box-arrow-left"></i>
                </td>
                <td v-else><i class="bi bi-box-arrow-right"></i></td>
                <td >{{ item[1] }}</td>
                <td>{{ item[2] }}</td>
                <td scope="col">STP</td>
                <td scope="col">STP %</td>
                <td>{{ item[4] }}</td>
                <td scope="col">TGT</td>
                <td>{{ item[3] }}</td>
                <td :class="{ 'table-success':item[5] > 0, 'table-danger':item[5] < 0  }">{{ item[5] }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import { useStore } from 'vuex'
export default {
    setup() {
        const store = useStore()

        const { report } = store.state.backtest.backtests[0]

        return{
            report
        }
    }
    

}
</script>

<style>

</style>