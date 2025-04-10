<template>
    <div class="row d-flex justify-content-center mx-auto mt-5" v-if="team">
        <div class="col-6 pt-6">
            <p><strong>Team:</strong> {{ team.value.teamName }}</p>
            <div class="mt-4 d-flex gap-2">
                <button class="btn btn-danger" @click="deleteTeam">Delete</button>
            </div>
        </div>
    </div>
    <div v-else>
        <p>Loading team details...</p>
    </div>
</template>
  
<script setup>
import { useRouter } from 'vue-router';
import { useFetchTeam, useDeleteTeam } from '../store/team';

const router = useRouter();
const { team } = useFetchTeam(router.currentRoute.value.params.teamId);

const deleteTeam = async () => {
    if (!team.value || !team.value.teamId) return;
    try {
        await useDeleteTeam(team.value.teamId);
    } catch (error) {
        console.error("Error deleting team:", error);
    }
};

</script>
