package com.eventmanagement.model;

import lombok.Data;

@Data
public class Manage {

    private int eventId;
    private String status;
    private int approvedBy;

}
