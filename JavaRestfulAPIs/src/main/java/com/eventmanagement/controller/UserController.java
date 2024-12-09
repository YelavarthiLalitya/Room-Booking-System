package com.eventmanagement.controller;

import com.eventmanagement.model.Role;
import com.eventmanagement.model.User;
import com.eventmanagement.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class UserController {
    @Autowired
    UserService userService;

    @PostMapping("/authenticate")
    public ResponseEntity<Map<String, Object>> login(@RequestBody User user) {
        // System.out.println(user);
        List<Map<String, Object>> validuserList = userService.validateLogin(user);
        if (validuserList != null && !validuserList.isEmpty() && validuserList.size() == 1) {
            Map<String, Object> validUser = validuserList.get(0);
            Map<String, Object> response = new HashMap<>();
            response.put("status", "success");
            response.put("error", "");
            response.put("id", validUser.get("id").toString());
            response.put("loginId", validUser.get("login_id").toString());
            response.put("name", validUser.get("name").toString());
            response.put("roleId", validUser.get("role_id").toString());
            response.put("role", validUser.get("role_name").toString());
            response.put("viewEvents", Boolean.valueOf(validUser.get("view_events").toString()));
            response.put("createEvent", Boolean.valueOf(validUser.get("create_events").toString()));
            response.put("manageEvent", Boolean.valueOf(validUser.get("approve_events").toString()));
            response.put("jwt", validUser.get("jwt").toString());
            return ResponseEntity.ok(response);
        } else {
            Map<String, Object> errorResponse = new HashMap<>();
            errorResponse.put("status", "failed");
            errorResponse.put("error", "Invalid credentials or user not found.");

            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(errorResponse);
        }
    }
}
