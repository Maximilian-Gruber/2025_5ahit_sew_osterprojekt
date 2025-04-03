<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-4 pt-6">
            <form>
                <div class="form-group">
                    <label for="eventNameField">Name</label>
                    <input v-model="form.eventName" type="text" class="form-control" id="eventNameField">
                </div>
                <div class="form-group">
                    <label for="descriptionField">Description</label>
                    <textarea v-model="form.description" class="form-control" id="descriptionField"></textarea>
                </div>
                <div class="form-group">
                    <label for="dateField">Date</label>
                    <input v-model="form.date" type="date" class="form-control" id="dateField">
                </div>
                <div class="form-group form-check">
                    <input v-model="form.isSeries" type="checkbox" class="form-check-input" id="isSeriesField">
                    <label class="form-check-label" for="isSeriesField">Is Series</label>
                </div>
                <div class="form-group">
                    <label for="teamIdField">Team ID</label>
                    <input v-model="form.teamId" type="text" class="form-control" id="teamIdField">
                </div>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary" v-on:click="submit">Create</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import { createEvent } from '../store/event';

export default {
    setup() {
        const form = ref({
            eventName: "",
            description: "",
            date: "",
            isSeries: false,
            teamId: "",
        });

        const submit = async (event) => {
            event.preventDefault();
            const formattedForm = { ...form.value, date: new Date(form.value.date).toISOString() };
            createEvent(formattedForm);
        };

        return {
            form,
            submit,
        };
    },
};
</script>

<style scoped>
.create-event-view {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input,
textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>