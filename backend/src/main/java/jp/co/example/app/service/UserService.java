package jp.co.example.app.service;

import java.util.Optional;
import jp.co.example.domain.model.User;
import jp.co.example.domain.repository.UserRepository;
import org.springframework.stereotype.Service;

@Service
public class UserService {
  private final UserRepository userRepository;

  public UserService(UserRepository userRepository) {
    this.userRepository = userRepository;
  }

  public Optional<User> getUserById(Long id) {
    return userRepository.findById(id);
  }
}
