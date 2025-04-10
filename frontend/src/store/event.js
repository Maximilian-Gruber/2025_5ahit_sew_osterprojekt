import { reactive, ref } from "vue";
import { apiGetEventList, apiGetEvent, apiDeleteEvent, apiCreateEvent, apiUpdateEvent, apiConfirmEvent, apiDeclineEvent} from "../api/event";
import { useLoadingStore } from "./loading";
import { useDialogStore } from "./dialog";
import router from "../router";
import { useAuthStore } from "./auth";


function useFetchEvents() {

    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    const eventList = reactive([
        {   eventId: "",
            eventName: "",
            description: "",
            date: "",
            isSeries: false,
            teamId: "",
        }
    ]);

    const fetchEvents = async () => {
        loadingStore.setLoading();

        try {
            console.log(authStore.access_token);
            const res = await apiGetEventList(authStore.access_token);
            eventList.value = res.data;
        } catch (err) {
            console.log(err);
        } finally {
            loadingStore.clearLoading();
        }
    };

    fetchEvents();

    return { eventList };
}

function useFetchEvent(eventId) {

    const loadingStore = useLoadingStore();
    const authStore = useAuthStore();

    const event = reactive([
        {   eventId: "",
            eventName: "",
            description: "",
            date: "",
            isSeries: false,
            teamId: "",
        }
    ]);

    const fetchEvent = async () => {
        loadingStore.setLoading();

        try {
            console.log(authStore.access_token);
            const res = await apiGetEvent(eventId, authStore.access_token);
            event.value = res.data;
        } catch (err) {
            console.log(err);
        } finally {
            loadingStore.clearLoading();
        }
    };

    fetchEvent();

    return { event };
}


function useConfirmEvent(eventId){
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    apiConfirmEvent(eventId, authStore.access_token)
    .then((res) => {
        console.log(res);
        dialogStore.setSuccess({
          title: "Confirming Event successful",
        });
        setTimeout(() => {
          router.push("/");
        },2010);
      })
      .catch((err) => {
        console.log(err);
        dialogStore.setError({
          title: "Confirming Event Failed",
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


function useDeclineEvent(eventId){
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    apiDeclineEvent(eventId, authStore.access_token)
    .then((res) => {
        console.log(res);
        dialogStore.setSuccess({
          title: "Declining Event successful",
        });
        setTimeout(() => {
          router.push("/");
        },2010);
      })
      .catch((err) => {
        console.log(err);
        dialogStore.setError({
          title: "Declining Event Failed",
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

function createEvent(form){
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    loadingStore.setLoading();
    console.log(form);

    apiCreateEvent(form, authStore.access_token)
    .then((res) => {
        console.log(res);
        dialogStore.setSuccess({
          title: "Create Event Success",
        });
        setTimeout(() => {
          router.push("/");
        },2010);
      })
      .catch((err) => {
        console.log(err);
        dialogStore.setError({
          title: "Create Event Failed",
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

function useDeleteEvent(eventId) {
    const loadingStore = useLoadingStore();
    const dialogStore = useDialogStore();
    const authStore = useAuthStore();

    loadingStore.setLoading();

    apiDeleteEvent(eventId, authStore.access_token)
        .then((res) => {
            console.log(res);
            dialogStore.setSuccess({
                title: "Event deleted successfully",
            });
            setTimeout(() => {
              router.push("/");
            },2010);
        })
        .catch((err) => {
            console.log(err);
            dialogStore.setError({
                title: "Failed to delete event",
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

export { useFetchEvents, useFetchEvent, useConfirmEvent, useDeclineEvent, createEvent, useDeleteEvent };