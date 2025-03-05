import request from './req';
import axios from 'axios';

export const apiGetEventList = () => axios.get('/events');
export const apiGetEvent = id => axios.get(`/events/${id}`);
export const apiCreateEvent = data => axios.post('/events', data);
export const apiUpdateEvent = (id, data) => axios.put(`/events/${id}`, data);
export const apiDeleteEvent = id => axios.delete(`/events/${id}`);
export const apiGetPlayersByEvent = id => axios.get(`/events/${id}/players`);
export const apiAddPlayerToEvent = (eventId, userId) => axios.post(`/events/${eventId}/players/${userId}`);
export const apiGetEventsByTeam = teamId => axios.get(`/teams/events/${teamId}`);
export const apiConfirmEvent = () => axios.post('/events/confirm');
export const apiDeclineEvent = () => axios.post('/events/decline');
