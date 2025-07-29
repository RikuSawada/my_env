package jp.co.example.domain.repository;

import java.util.Optional;
import jp.co.example.domain.model.User;

public interface UserRepository {
  Optional<User> findById(Long id);
}
