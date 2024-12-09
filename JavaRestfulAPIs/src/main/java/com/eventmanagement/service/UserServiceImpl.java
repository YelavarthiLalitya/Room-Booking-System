package com.eventmanagement.service;

import com.eventmanagement.model.User;
import com.eventmanagement.repository.UserRepository;
import com.eventmanagement.utils.JwtTokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    UserRepository userRepository;
    @Autowired
    JwtTokenUtil jwtTokenUtil;

    @Override
    public List<Map<String, Object>> validateLogin(User user) {
        List<Map<String, Object>> validuserList = userRepository.validateLogin(user);
        if (validuserList != null && !validuserList.isEmpty() && validuserList.size() == 1) {
            String token = jwtTokenUtil.generateToken(user.getLoginId());
            Object jwtObject = token;
            validuserList.get(0).put("jwt", jwtObject);
            // Map<String, Object> validUser =
            // validUser.put("jwt", jwtObject);
        }
        return validuserList;
    }

    @Override
    public Map<String, Object> getUserRole(int userId) {
        return userRepository.getUserRole(userId);
    }

}
