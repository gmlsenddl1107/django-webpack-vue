<template>
    <v-app>
        <v-navigation-drawer
                v-model="drawer"
                app
                clipped
                color="light-green lighten-1"
        >
            <v-list dense>
                <v-list-item v-for="menu in menus" :key="menu.title" :to="menu.link">
                    <v-list-item-icon>
                        <v-icon>{{ menu.icon }}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{menu.title}}</v-list-item-title>
                    </v-list-item-content>

                </v-list-item>
                <v-list-item>
                    <v-btn v-on:click="logout" v-if="token !== null">
                        Logout
                    </v-btn>

                </v-list-item>

            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                app
                clipped-left
                color="light-green darken-3"

        >
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
            <v-toolbar-title class="nicefont">KP-OP</v-toolbar-title>
        </v-app-bar>

        <v-content class="ma-3">

            <router-view></router-view>


        </v-content>

        <v-footer app>

        </v-footer>
    </v-app>
</template>

<script>
    import router from "./router"

    export default {
        name: "app",
        components: {},
        data: () => ({
            drawer: null,
            menus: [{title: 'gpu', link: '/gpu', icon: 'mdi-view-dashboard'},
                {title: 'about', link: '/about',icon: 'mdi-help-box' }]
        }),
        created() {

        },
        methods: {
            logout: function () {

            }

        }
    }
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');

    .nicefont {
        font-size: 26px;
        font-family: 'Alatsi', sans-serif;
    }
</style>