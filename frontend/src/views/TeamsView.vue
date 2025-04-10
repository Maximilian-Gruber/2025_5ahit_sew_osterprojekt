<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
            <table class="table">
            <thead>
                <tr>
                    <th scope="col">Team</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(team) in teams" :key="team.teamId" @click="pushToTeamView(team)" class="hover-effect">
                    <td>{{ team.teamName }}</td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>
  
<script setup>
import { useFetchTeams } from '../store/team';
import { useRouter } from 'vue-router';

const { teams } = useFetchTeams();

const router = useRouter();

function pushToTeamView(team) {
    router.push({ name: 'Team', params: { teamId: team.teamId } });
}

</script>


<style scoped>

.hover-effect:hover {
    cursor: pointer;
    background-color: rgb(195, 193, 193);
}
</style>