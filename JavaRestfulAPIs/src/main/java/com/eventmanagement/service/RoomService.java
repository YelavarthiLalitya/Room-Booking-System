package com.eventmanagement.service;

import com.eventmanagement.model.RoomInfo;

import java.util.List;
import java.util.Map;

public interface RoomService {

    List<Map<String, Object>> getAvailableRoomsInfo(RoomInfo roomInfo);
}
