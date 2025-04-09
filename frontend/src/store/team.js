// store/team.js
import { ref } from "vue";
import { apiGetTeam, apiGetTeamsList, apiCreateTeam } from "../api/team";
import { useLoadingStore } from "./loading";
import { useDialogStore } from "./dialog";
import { useAuthStore } from "./auth";
import router from "../router";


function useFetchTeams() {
    const teams = ref([]);
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    const fetchTeams = async () => {
        loadingStore.setLoading();

        try {
            console.log("Token:", authStore.access_token);
            const res = await apiGetTeamsList(authStore.access_token);
            teams.value = res.data;
        } catch (err) {
            console.error("Error fetching teams:", err);
        } finally {
            loadingStore.clearLoading();
        }
    };

    fetchTeams();

    return { teams };
}


function useFetchTeam(teamId) {

    const loadingStore = useLoadingStore();
    const authStore = useAuthStore();

    const team = reactive([
        {   teamId: "",
            teamName: "",
            coachId: "",
        }
    ]);

    const fetchTeam = async () => {
        loadingStore.setLoading();

        try {
            console.log(authStore.access_token);
            const res = await apiGetTeam(teamId, authStore.access_token);
            team.value = res.data;
        } catch (err) {
            console.log(err);
        } finally {
            loadingStore.clearLoading();
        }
    };

    fetchTeam();

    return { team };
}


function createTeam(form){
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    loadingStore.setLoading();
    console.log(form);

    apiCreateTeam(form, authStore.access_token)
    .then((res) => {
        console.log(res);
        dialogStore.setSuccess({
          title: "Create Team Success",
        });
        setTimeout(() => {
          router.push("/");
        },2010);
      })
      .catch((err) => {
        console.log(err);
        dialogStore.setError({
          title: "Create Team Failed",
          firstLine: err.response?.data?.detail || "An unexpected error occurred",
        });
      })
      .finally(() => {
        loadingStore.clearLoading();
        setTimeout(() => {
          dialogStore.reset();
        }, 2000);
      });
}

export { useFetchTeams, useFetchTeam, createTeam };
