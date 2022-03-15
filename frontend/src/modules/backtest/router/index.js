import isAuthenticatedGuard from '@/modules/auth/router/auth-guard'

export default {

    name: 'backtest',
    component: () => import(/* webpackChunkName: "backtest" */ '@/modules/backtest/layouts/BacktestLayout.vue'),
    children: [
        {
            path: '/backtest',
            name: 'backtest',
            beforeEnter: [ isAuthenticatedGuard ],
            component: () => import(/* webpackChunkName: "backtest" */ '@/modules/backtest/views/BackTest.vue'),
        },
        {
            path: '/backtestResult',
            name: 'backtestResult',
            beforeEnter: [ isAuthenticatedGuard ],
            component: () => import(/* webpackChunkName: "backtestResult" */ '@/modules/backtest/views/BacktestResult.vue'),
        },
        {
            path: '/profile',
            name: 'profile',
            beforeEnter: [ isAuthenticatedGuard ],
            component: () => import(/* webpackChunkName: "profile" */ '@/modules/auth/views/Profile.vue'),
        },
    ]
}