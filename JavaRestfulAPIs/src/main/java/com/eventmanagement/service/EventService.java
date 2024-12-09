package com.eventmanagement.service;

import com.eventmanagement.model.Event;
import com.eventmanagement.model.Manage;
import com.eventmanagement.repository.EventRepository;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

public interface EventService {

    int createEvent(Event event);

    Event getEventByName(String name);

    List<Map<String, Object>> getEvents(int userId, int roleId);

    int manageEvent(Manage manage);

}
