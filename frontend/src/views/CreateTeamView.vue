<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-4 pt-6">
            <form>
                <div class="form-group">
                    <label for="teamNameField">Name</label>
                    <input v-model="form.teamName" type="text" class="form-control" id="teamNameField">
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
import { createTeam } from '../store/team';

export default {
    setup() {
        const form = ref({
            teamName: "",
            coachId: "",
        })

        const submit = async (team) => {
            team.preventDefault();
            await createTeam(form.value);
        }

        return {
            form, 
            submit,
        }
    }
}

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
textarea,
select {
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
