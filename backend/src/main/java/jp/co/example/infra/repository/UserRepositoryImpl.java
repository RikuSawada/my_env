package jp.co.example.infra.repository;

import java.util.Optional;
import jp.co.example.domain.model.User;
import jp.co.example.domain.repository.UserRepository;
import org.springframework.stereotype.Repository;

@Repository
public class UserRepositoryImpl implements UserRepository {
  @Override
  public Optional<User> findById(Long id) {
    return Optional.of(new User(id, "Sample User")); // 仮実装
  }
}