package com.eventmanagement.controller;

import com.eventmanagement.model.RoomInfo;
import com.eventmanagement.service.RoomService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class RoomController {

    @Autowired
    RoomService roomService;

    @PostMapping("/rooms/available")
    public ResponseEntity<?> getAvailableRoomsInfo(@RequestBody RoomInfo roomInfo) {
        // System.out.println(roomInfo);
        List<Map<String, Object>> roomsList = roomService.getAvailableRoomsInfo(roomInfo);
        List<Map<String, Object>> roomsListForResponse = new ArrayList<Map<String, Object>>();
        if (roomsList == null || roomsList.isEmpty()) {
            Map<String, Object> errorResponse = new HashMap<>();
            errorResponse.put("errorCode", "NO_DATA_FOUND");
            errorResponse.put("message", "No rooms found for the given criteria.");
            errorResponse.put("status", 404);
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
        } else {
            for (Map<String, Object> item : roomsList) {
                Map<String, Object> tempMap = new HashMap<String, Object>();
                tempMap.put("id", item.get("id"));
                tempMap.put("name", item.get("name"));
                tempMap.put("type", item.get("room_type"));
                tempMap.put("capacity", item.get("capacity"));
                tempMap.put("location", item.get("location"));
                roomsListForResponse.add(tempMap);
            }
        }
        return ResponseEntity.ok(roomsListForResponse);
    }
}
