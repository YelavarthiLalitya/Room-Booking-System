package com.eventmanagement.repository;

import com.eventmanagement.model.Event;
import com.eventmanagement.model.Manage;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.jdbc.core.JdbcTemplate;

@Repository
public class EventRepository {

    @Autowired
    NamedParameterJdbcTemplate namedParameterJdbcTemplate;

    public int createEvent(Event event) {
        String insertQuery = "INSERT INTO event (event_name, event_desc, capacity, event_date, " +
                "event_start_time, event_end_time, booking_status, room_id, user_id) " +
                "VALUES (:event_name, :event_desc, :capacity, :event_date, :event_start_time, :event_end_time, " +
                ":booking_status, :room_id, :user_id)";

        MapSqlParameterSource params = new MapSqlParameterSource()
                .addValue("event_name", event.getName())
                .addValue("event_desc", event.getDescription())
                .addValue("capacity", event.getExpectedStrength()) // Safe integer parsing
                .addValue("event_date", event.getDate())
                .addValue("event_start_time", event.getStartTime())
                .addValue("event_end_time", event.getEndTime())
                .addValue("booking_status", event.getBookingStatus())
                .addValue("room_id", event.getRoomId())
                .addValue("user_id", event.getUserId());
        int count = namedParameterJdbcTemplate.update(insertQuery, params);
        return count;

    }

    public List<Map<String, Object>> getEvents(int userId, int roleId) {
        List<Map<String, Object>> eventList = new ArrayList<>();
        Map<String, Object> params = new HashMap<>();
        String query = "select * from event";
        if (roleId == 3) {
            // query = "select * from event inner join user_mst where user_id=:userId and
            // role_id=:roleId";
            query = "select e.*, u.name as user_name, r.name as room_name from event e " +
                    "inner join user_mst u on e.user_id=u.id " +
                    "inner join room_mst r on e.room_Id=r.Id " +
                    "where e.user_id=:userId and r.id=:roleId";
            params.put("userId", userId);
            params.put("roleId", roleId);

        }
        eventList = namedParameterJdbcTemplate.queryForList(query, params);
        return eventList;
    }

    public int manageEvent(Manage manage) {
        String updateStmt = "update event set booking_status=:status,approved_by=:approvedby where id=:eventid";

        /*
         * "INSERT INTO event (event_name, event_desc, capacity, event_date, " +
         * "event_start_time, event_end_time, booking_status, room_id, user_id) " +
         * "VALUES (:event_name, :event_desc, :capacity, :event_date, :event_start_time, :event_end_time, "
         * +
         * ":booking_status, :room_id, :user_id)";
         */

        MapSqlParameterSource params = new MapSqlParameterSource()
                .addValue("status", manage.getStatus())
                .addValue("approvedby", manage.getApprovedBy())
                .addValue("eventid", manage.getEventId());
        int count = namedParameterJdbcTemplate.update(updateStmt, params);
        return count;

    }

}
