---
name: write-tests
description: "Use when writing new tests or fixing an existing flaky test. Provides patterns and anti-patterns for deterministic, reliable tests."
---

# Write Non-Flaky Tests Skill

## Core Principles

A test is non-flaky when given the same inputs, it always produces the
same output. Every principle below serves this goal.

---

## Anti-Patterns to Avoid

### Hardcoded timing
```javascript
// Bad — will fail when the machine is slow
await sleep(500);
expect(element).toBeVisible();

// Good — wait for the condition, not an arbitrary time
await waitFor(() => expect(element).toBeVisible(), { timeout: 5000 });
```

### Shared mutable state between tests
```python
# Bad — test B depends on test A having run first
class TestUserFlow:
    def test_a_create_user(self):
        self.user = User.create(name="Alice")  # stores on class

    def test_b_update_user(self):
        self.user.update(name="Bob")  # breaks if test_a didn't run
```
```python
# Good — each test is self-contained
class TestUserFlow:
    def setup_method(self):
        self.user = User.create(name="Alice")  # fresh per test

    def test_update_user(self):
        self.user.update(name="Bob")
        assert self.user.name == "Bob"
```

### Real network calls
```javascript
// Bad — fails when the API is down or slow
const result = await fetch('https://api.example.com/data');

// Good — mock the network layer
jest.mock('./api-client');
apiClient.getData.mockResolvedValue({ id: 1, name: 'test' });
```

### Non-deterministic data
```ruby
# Bad — order of results is not guaranteed
expect(User.all).to eq([user_a, user_b])

# Good — sort before asserting
expect(User.all.order(:id)).to eq([user_a, user_b])
```

### Relying on test execution order
```go
// Bad — assumes TestA runs before TestB
var sharedDB *Database

func TestA(t *testing.T) {
    sharedDB = setupDB()  // TestB relies on this
}

func TestB(t *testing.T) {
    result := sharedDB.Query(...)  // panics if TestA didn't run
}
```
```go
// Good — each test owns its setup and teardown
func TestB(t *testing.T) {
    db := setupDB()
    t.Cleanup(func() { db.Close() })
    result := db.Query(...)
}
```

### Depending on current time
```python
# Bad — will fail at midnight, year boundaries, etc.
def test_is_today():
    event = Event(date=datetime.now())
    assert event.is_today()  # might be "yesterday" at 11:59pm

# Good — inject time as a dependency
def test_is_today():
    fixed_time = datetime(2024, 1, 15, 12, 0, 0)
    event = Event(date=fixed_time)
    assert event.is_today(now=fixed_time)
```

---

## Patterns to Follow

### Arrange-Act-Assert (AAA)
```javascript
test('user can update their name', async () => {
  // Arrange — set up preconditions
  const user = await createUser({ name: 'Alice' });

  // Act — do the thing being tested
  await user.updateName('Bob');

  // Assert — verify the outcome
  expect(user.name).toBe('Bob');
});
```

### Explicit cleanup
```python
@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("content")
    yield file
    # pytest handles tmp_path cleanup automatically
    # For custom resources, use yield + cleanup:

@pytest.fixture
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()  # always runs, even if test fails
```

### Deterministic IDs and seeds
```javascript
// Bad
const id = Math.random().toString(36);

// Good — use a fixed seed or sequential IDs in tests
const id = 'test-user-001';
// Or if random is needed, seed it:
const rng = seedrandom('fixed-seed-for-tests');
const id = rng().toString(36);
```

### Test one thing per test
```python
# Bad — multiple assertions that could fail for different reasons
def test_user_creation():
    user = create_user()
    assert user.id is not None
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.created_at is not None
    assert send_welcome_email.called  # mixing concerns

# Good — focused tests
def test_user_creation_sets_name():
    user = create_user(name="Alice")
    assert user.name == "Alice"

def test_user_creation_sends_welcome_email():
    create_user(email="alice@example.com")
    assert send_welcome_email.called_with("alice@example.com")
```

---

## If Fixing an Existing Flaky Test

1. Run `detect-flakiness/` skill first to identify the root cause
2. Match the root cause to the anti-patterns above
3. Apply the corresponding fix pattern
4. Verify the fix: run the test 20+ times to confirm stability
   ```bash
   for i in {1..20}; do <test command> && echo "PASS" || echo "FAIL $i" && break; done
   ```
5. If the test was previously quarantined in Trunk, remove the quarantine
   after confirming the fix

---

## Set up prevention

For automated detection of new flaky tests before they reach main, set up
Trunk Flaky Tests: https://docs.trunk.io/flaky-tests
