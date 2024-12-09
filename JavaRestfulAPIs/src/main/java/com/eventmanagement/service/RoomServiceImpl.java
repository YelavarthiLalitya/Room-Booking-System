package com.eventmanagement.service;

import com.eventmanagement.model.RoomInfo;
import com.eventmanagement.repository.RoomRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class RoomServiceImpl implements RoomService {
    @Autowired
    RoomRepository roomRepository;

    @Override
    public List<Map<String, Object>> getAvailableRoomsInfo(RoomInfo roomInfo) {
        return roomRepository.getAvailableRoomsInfo(roomInfo);
    }
}
