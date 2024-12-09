package com.eventmanagement.controller;

import com.eventmanagement.model.Event;
import com.eventmanagement.service.EventService;
import com.eventmanagement.service.UserService;
import com.eventmanagement.model.Manage;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class EventController {

    @Autowired
    EventService eventService;

    @Autowired
    UserService userService;

    @PostMapping("/create")
    public ResponseEntity<Map<String, Object>> createEvent(@RequestBody Event event) {
        // System.out.println(event);
        Map<String, Object> response = new HashMap<>();
        // validate user has permission to create event, if use has no permission then
        // return Unauthorized response.
        Map<String, Object> userRoleInfo = userService.getUserRole(event.getUserId());
        if (userRoleInfo != null && !userRoleInfo.isEmpty()) {
            if (!Boolean.valueOf(userRoleInfo.get("create_events").toString())) {
                response.put("status", "failed");
                response.put("error", "User is not authorised to create event");
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(response);
            }
        }
        int count = eventService.createEvent(event);
        if (count == 1) {
            response.put("status", "success");
            response.put("error", "");
        } else {
            response.put("status", "failed");
            response.put("error", "Error creating event");
        }
        return ResponseEntity.ok(response);
    }

    @GetMapping("/events/user/{userId}/role/{roleId}")
    public ResponseEntity<?> getEvents(@PathVariable("userId") int userId, @PathVariable("roleId") int roleId) {
        // System.out.println("userid: " + userId + " roleid: " + roleId);
        List<Map<String, Object>> eventList = eventService.getEvents(userId, roleId);
        List<Map<String, Object>> eventListTemp = new ArrayList<Map<String, Object>>();
        if (eventList == null || eventList.isEmpty()) {
            Map<String, Object> errorResponse = new HashMap<>();
            errorResponse.put("errorCode", "NO_DATA_FOUND");
            errorResponse.put("message", "No events found for the given user and role.");
            errorResponse.put("status", 404);
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
        } else {
            for (Map<String, Object> item : eventList) {
                Map<String, Object> tempMap = new HashMap<String, Object>();
                tempMap.put("id", item.get("id"));
                tempMap.put("eventName", item.get("event_name"));
                tempMap.put("eventDesc", item.get("event_desc"));
                tempMap.put("eventDate", item.get("event_date"));
                tempMap.put("startTime", item.get("event_start_time"));
                tempMap.put("endTime", item.get("event_end_time"));
                tempMap.put("bookingStatus", item.get("booking_status"));
                tempMap.put("requestorName", item.get("user_name"));
                tempMap.put("roomName", item.get("room_name"));
                eventListTemp.add(tempMap);
            }
        }
        return ResponseEntity.ok(eventListTemp);
    }

    @PostMapping("/manage")
    public ResponseEntity<Map<String, Object>> manageEvent(@RequestBody Manage manage) {
        System.out.println(manage);
        Map<String, Object> response = new HashMap<>();
        // validate user has permission to create event, if use has no permission then
        // return Unauthorized response.
        // Map<String, Object> userRoleInfo =
        // userService.getUserRole(event.getUserId());
        /*
         * if (userRoleInfo != null && !userRoleInfo.isEmpty()) {
         * if (!Boolean.valueOf(userRoleInfo.get("create_events").toString())) {
         * response.put("status", "failed");
         * response.put("error", "User is not authorised to create event");
         * return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(response);
         * }
         * }
         */
        int count = eventService.manageEvent(manage);
        if (count == 1) {
            response.put("status", "success");
            response.put("error", "");
        } else {
            response.put("status", "failed");
            response.put("error", "Error creating event");
        }

        return ResponseEntity.ok(response);
    }
}
