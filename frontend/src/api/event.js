import request from './req';
import axios from 'axios';

export const apiGetEventList = access_token => axios.get('/events', { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiGetEvent = (id, access_token) => axios.get(`/events/${id}`, { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiCreateEvent = data => axios.post('/events', data);
export const apiUpdateEvent = (id, data) => axios.put(`/events/${id}`, data);
export const apiDeleteEvent = id => axios.delete(`/events/${id}`);
export const apiGetPlayersByEvent = id => axios.get(`/events/${id}/players`);
export const apiAddPlayerToEvent = (eventId, userId) => axios.post(`/events/${eventId}/players/${userId}`);
export const apiGetEventsByTeam = teamId => axios.get(`/teams/events/${teamId}`);
export const apiConfirmEvent = (eventId, access_token) => axios.post(`/events/confirm/?eventId=${eventId}`, { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
export const apiDeclineEvent = (eventId, access_token) => axios.post(`/events/decline/?eventId=${eventId}`, { headers: { "Authorization": `Bearer ${access_token}`, "Content-Type": "application/json" }});
