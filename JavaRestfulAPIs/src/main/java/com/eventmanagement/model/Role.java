package com.eventmanagement.model;

import lombok.Data;

@Data
public class Role {
    public static final String SUPER_ADMIN = "Super Admin";
    public static final String APPROVAL_ADMIN = "Approval Admin";
    public static final String ROOM_BOOKING_ADMIN = "Room Booking Admin";
    public static final String STANDARD_USER = "Standard User";

    private String name;

    public Role() {
    }

    public Role(String name) {
        this.name = name;
    }

}
