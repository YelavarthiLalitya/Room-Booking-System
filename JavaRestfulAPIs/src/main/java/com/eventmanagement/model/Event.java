package com.eventmanagement.model;

import lombok.Data;

@Data
public class Event {
    private String name;
    private String description;
    private String date;
    private String startTime;
    private String endTime;
    private String expectedStrength;
    private int roomId;
    private int userId;
    private String bookingStatus;

}
