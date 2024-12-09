package com.eventmanagement.repository;

import com.eventmanagement.model.RoomInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository
public class RoomRepository {
    @Autowired
    JdbcTemplate jdbcTemplate;

    public List<Map<String, Object>> getAvailableRoomsInfo(RoomInfo roomInfo) {
        String query = "SELECT r.* FROM room_mst r LEFT JOIN event e ON e.room_id = r.id " +
                " AND e.booking_status <> 'Approved' AND e.event_date = '" + roomInfo.getEventDate() + "' " +
                " AND e.event_start_time < '" + roomInfo.getEndTime() + "'  " +
                " AND e.event_end_time > '" + roomInfo.getStartTime() + "' " +
                " WHERE (e.event_date >= '" + roomInfo.getEventDate() + "' OR e.event_date IS NULL)" +
                "AND r.capacity >= " + roomInfo.getCapacity();
        /*
         * String query =
         * "SELECT r.* FROM room_mst r LEFT JOIN event e ON e.room_id = r.id " +
         * "  AND e.booking_status <> 'Approved' AND e.event_date = '" +
         * roomInfo.getEventDate() + "' " +
         * " AND e.event_start_time < '" + roomInfo.getEndTime() +
         * "' AND e.event_end_time > '"
         * + roomInfo.getStartTime()
         * + "' WHERE r.available_from_date >= '" + roomInfo.getEventDate() + "' ";
         */
        // +
        // " AND r.available_from_time > '" + roomInfo.getEndTime() + "' AND e.room_id
        // IS NULL;\n";
        System.out.println(query);
        List<Map<String, Object>> roomMap = jdbcTemplate.queryForList(query);
        return roomMap;
    }

}
