package com.eventmanagement.model;

import lombok.Data;

@Data
public class RoomInfo {
    private String eventDate;
    private String startTime;
    private String endTime;
    private int capacity;

}
