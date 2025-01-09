CREATE TABLE users (
    id SERIAL PRIMARY KEY,        -- ID tự động tăng, là khóa chính
    username VARCHAR(50) NOT NULL UNIQUE, -- Tên đăng nhập, phải là duy nhất
    password VARCHAR(255) NOT NULL, -- Mật khẩu, nên được lưu ở dạng mã hóa
    role VARCHAR(20) NOT NULL      -- Vai trò (admin, user, v.v.)
);

INSERT INTO users (username, password, role)
VALUES 
('admin', '123', 'admin'),
('user', '123', 'user'),
('owner', '123', 'owner');

SELECT * FROM users;
