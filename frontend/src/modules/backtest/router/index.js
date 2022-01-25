import isAuthenticatedGuard from '@/modules/auth/router/auth-guard'
export default {
    name: 'backtest',
    component: () => import(/* webpackChunkName: "backtest" */ '@/modules/backtest/layouts/BacktestLayout.vue'),
    children: [
        {
            path: '/backtest',
            name: 'backtest',
            component: () => import(/* webpackChunkName: "backtest" */ '@/modules/backtest/views/BackTest.vue'),
        },
        {
            path: '/profile',
            name: 'profile',
            beforeEnter: [ isAuthenticatedGuard ],
            component: () => import(/* webpackChunkName: "profile" */ '@/modules/auth/views/Profile.vue'),
        },
    ]
}