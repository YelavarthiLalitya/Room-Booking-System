package com.eventmanagement.service;

import com.eventmanagement.model.User;

import java.util.List;
import java.util.Map;

public interface UserService {

    List<Map<String, Object>> validateLogin(User user);

    Map<String, Object> getUserRole(int userId);
}
