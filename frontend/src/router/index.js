import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import LogoutView from '../views/LogoutView.vue'
import RefreshView from '../views/RefreshView.vue'
import EventView from '../views/EventView.vue'
import CreateEventView from '../views/CreateEventView.vue'
import CreateTeamView from '../views/CreateTeamView.vue'
import TeamsView from '../views/TeamsView.vue'
import TeamView from '../views/TeamView.vue'
import { useAuthStore } from '../store/auth'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },
    {
        path: '/logout',
        name: 'Logout',
        component: LogoutView,
    },
    {
        path: '/refresh',
        name: 'Refresh',
        component: RefreshView,
    },
    {
        path: '/event/:eventId',
        name: 'Event',
        component: EventView,
    },
    {
        path: '/event/create',
        name: 'CreateEvent',
        component: CreateEventView,
        meta: { requiresAuth: true },
    },
    {
        path: '/team/create',
        name: 'CreateTeam',
        component: CreateTeamView,
        meta: { requiresAuth: true },
    },
    {
        path: '/teams/',
        name: 'Teams',
        component: TeamsView,
        meta: { requiresAuth: true },
    },
    {
        path: '/teams/:teamId',
        name: 'Team',
        component: TeamView,
        meta: { requiresAuth: true },
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

router.beforeEach((to, from , next) => {
    const auth = useAuthStore();
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (auth.isAuthenticated) {
            next();
            return;
        }
        next("/login");
    } else {
        next();
    }

})

export default router;