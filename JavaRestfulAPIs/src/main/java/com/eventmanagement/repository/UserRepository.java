package com.eventmanagement.repository;

import com.eventmanagement.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository
public class UserRepository {

    @Autowired
    JdbcTemplate jdbcTemplate;

    public List<Map<String, Object>> validateLogin(User user) {
        String query = "SELECT um.*, rm.* FROM user_mst um " +
                "INNER JOIN role_mst rm ON rm.id = um.role_id " +
                "WHERE um.login_id = '" + user.getLoginId() + "' " +
                "AND um.password = '" + user.getPassword() + "'";

        return jdbcTemplate.queryForList(query);
    }

    public Map<String, Object> getUserRole(int userId) {
        String query = "select u.id userId, r.id roleId,u.*,r.* from user_mst u inner join role_mst r on (r.id=role_id) where u.id="
                + userId + "";
        return jdbcTemplate.queryForMap(query);
    }

}
