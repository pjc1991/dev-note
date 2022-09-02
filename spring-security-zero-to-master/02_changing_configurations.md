# Changing Default Configurations of Spring Security

## WebSecurityConfigurerAdapter

```java
@Configuration
public class WebSecurityConfigurerAdapter extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/myAccount").authenticated()
                .antMatchers("/myBalance").authenticated()
                .and()
            .formLogin().and()
            .httpBasic();
    }
}
```