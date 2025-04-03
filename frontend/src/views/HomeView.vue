<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
            <table class="table">
            <thead>
                <tr>
                    <th scope="col">Date</th>
                    <th scope="col">Event</th>
                    <th scope="col">Description</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(event) in eventList.value" :key="event.eventId" @click="pushToEventView(event)" class="hover-effect">
                    <td>{{ new Date(event.date).toLocaleString() }}</td>
                    <td>{{ event.eventName }}</td>
                    <td>{{ event.description }}</td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>
  
<script setup>

import { useFetchEvents } from '../store/event';
const { eventList } = useFetchEvents();
console.log(eventList);

import { useRouter } from 'vue-router';
const router = useRouter();

function pushToEventView(event) {
    console.log('pushToEventView', event.eventId);
    router.push({ name: 'Event', params: { eventId: event.eventId } });
} 


</script>

<style scoped>

.hover-effect:hover {
    cursor: pointer;
    background-color: rgb(195, 193, 193);
}
</style>