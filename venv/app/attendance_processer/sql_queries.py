


create_table = """CREATE TABLE `attendance` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                                        `meeting_name` VARCHAR(255) NOT NULL,
                                                        `meeting_start_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                        `meeting_end_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                        `name` VARCHAR(255) NOT NULL,
                                                        `attendee_email` VARCHAR(255) NOT NULL,
                                                        `join_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                        `leave_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                                        `attendance_duration` INT,
                                                        `connection_type` VARCHAR(255) );"""
                                                        
insert_row = """INSERT INTO `attendance`( `meeting_name`,
                                                `meeting_start_time`,
                                                `meeting_end_time`,
                                                `name`,
                                                `attendee_email`,
                                                `join_time`,
                                                `leave_time`,
                                                `attendance_duration`,
                                                `connection_type`)
                                                VALUES
                                                (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
                                                
select_row = """SELECT * FROM `attendance` WHERE `meeting_name`=%s and
                                                `meeting_start_time`=%s and
                                                `meeting_end_time`=%s and
                                                `name`=%s and
                                                `attendee_email`=%s and
                                                `join_time`=%s and
                                                `leave_time`=%s and
                                                `attendance_duration`=%s and
                                                `connection_type`=%s;"""

select_query = "SELECT * FROM `attendance`;"
