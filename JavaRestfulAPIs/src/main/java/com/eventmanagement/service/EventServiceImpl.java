package com.eventmanagement.service;

import com.eventmanagement.model.Event;
import com.eventmanagement.model.Manage;
import com.eventmanagement.repository.EventRepository;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class EventServiceImpl implements EventService {
    @Autowired
    EventRepository eventRepository;

    public int createEvent(Event event) {
        int count = eventRepository.createEvent(event);
        return count;

    }

    public Event getEventByName(String name) {
        return null;
    }

    @Override
    public List<Map<String, Object>> getEvents(int userId, int roleId) {
        return eventRepository.getEvents(userId, roleId);
    }

    @Override
    public int manageEvent(Manage manage) {
        return eventRepository.manageEvent(manage);
    }

}
