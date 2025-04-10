<template>
    <div class="row d-flex justify-content-center mx-auto mt-5" v-if="event">
        <div class="col-6 pt-6">
            <h1>{{ event.value.eventName }}</h1>
            <p><strong>Event:</strong> {{ event.value.eventName }}</p>
            <p><strong>Date:</strong> {{ formattedDate }}</p>
            <p><strong>Description:</strong> {{ event.value.description }}</p>
            <p><strong>Is Series:</strong> {{ event.value.isSeries }}</p>
            <p><strong>Team ID:</strong> {{ event.value.teamId }}</p>

            <div class="mt-4 d-flex gap-2">
                <button class="btn btn-success" @click="confirmEvent">Confirm</button>
                <button class="btn btn-danger" @click="declineEvent">Decline</button>
            </div>
        </div>
    </div>
    <div v-else>
        <p>Loading event details...</p>
    </div>
</template>
  
<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useFetchEvent, useConfirmEvent, useDeclineEvent } from '../store/event';

const router = useRouter();
const { event } = useFetchEvent(router.currentRoute.value.params.eventId);

const formattedDate = computed(() => {
    if (!event.value || !event.value.date) {
        return 'Invalid Date';
    }
    
    const parsedDate = new Date(event.value.date);
    
    if (isNaN(parsedDate)) {
        console.warn("Ungültiges Datum erhalten:", event.value.date);
        return 'Invalid Date';
    }

    return parsedDate.toLocaleString();
});

const confirmEvent = async () => {
    if (!event.value?.eventId) return;
    try {
        await useConfirmEvent(event.value.eventId);
        alert('Event confirmed successfully!');
    } catch (error) {
        console.error("Error confirming event:", error);
        alert('Failed to confirm event.');
    }
};

const declineEvent = async () => {
    if (!event.value?.eventId) return;
    try {
        await useDeclineEvent(event.value.eventId);
        alert('Event declined successfully!');
    } catch (error) {
        console.error("Error declining event:", error);
        alert('Failed to decline event.');
    }
};

</script>
